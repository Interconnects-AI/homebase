#!/usr/bin/env python3
"""
Chroma-based semantic search for Interconnects posts.

This script creates a vector database of all posts and enables semantic search
across the entire corpus. It chunks posts into sections and creates embeddings
for each chunk, allowing for concept-based rather than keyword-based search.
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Tuple
import chromadb
from chromadb.config import Settings
import tiktoken


class InterconnectsSearch:
    def __init__(self, chroma_dir: str = "./chroma_db"):
        """Initialize the search system with Chroma vector database."""
        self.chroma_dir = Path(chroma_dir)
        self.chroma_dir.mkdir(exist_ok=True)
        
        # Initialize Chroma with persistent storage
        self.client = chromadb.PersistentClient(path=str(self.chroma_dir))
        
        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name="interconnects_posts",
            metadata={"hnsw:space": "cosine"}
        )
        
        # Initialize tokenizer for chunk size estimation
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
        
    def chunk_text(self, text: str, max_tokens: int = 500, overlap_tokens: int = 50) -> List[str]:
        """
        Split text into overlapping chunks of approximately max_tokens size.
        
        Args:
            text: Text to chunk
            max_tokens: Maximum tokens per chunk
            overlap_tokens: Number of tokens to overlap between chunks
        
        Returns:
            List of text chunks
        """
        # Split by paragraphs first
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        chunks = []
        current_chunk = ""
        current_tokens = 0
        
        for paragraph in paragraphs:
            para_tokens = len(self.tokenizer.encode(paragraph))
            
            # If adding this paragraph would exceed max_tokens, save current chunk
            if current_tokens + para_tokens > max_tokens and current_chunk:
                chunks.append(current_chunk.strip())
                
                # Start new chunk with overlap
                if overlap_tokens > 0:
                    # Take last few sentences for overlap
                    sentences = current_chunk.split('. ')
                    overlap_text = '. '.join(sentences[-2:]) if len(sentences) > 1 else ""
                    overlap_token_count = len(self.tokenizer.encode(overlap_text))
                    
                    if overlap_token_count <= overlap_tokens:
                        current_chunk = overlap_text + ("\n\n" if overlap_text else "") + paragraph
                        current_tokens = overlap_token_count + para_tokens
                    else:
                        current_chunk = paragraph
                        current_tokens = para_tokens
                else:
                    current_chunk = paragraph
                    current_tokens = para_tokens
            else:
                # Add paragraph to current chunk
                if current_chunk:
                    current_chunk += "\n\n" + paragraph
                else:
                    current_chunk = paragraph
                current_tokens += para_tokens
        
        # Add final chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def extract_frontmatter_and_content(self, file_path: Path) -> Tuple[Dict, str]:
        """Extract YAML frontmatter and content from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    import yaml
                    frontmatter = yaml.safe_load(parts[1])
                    body_content = parts[2].strip()
                    return frontmatter, body_content
            
            return {}, content
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return {}, ""
    
    def index_posts(self, public_dir: str = "./public"):
        """Index all posts in the public directory."""
        public_path = Path(public_dir)
        if not public_path.exists():
            print(f"Public directory {public_dir} does not exist")
            return
        
        # Clear existing collection
        self.client.delete_collection("interconnects_posts")
        self.collection = self.client.create_collection(
            name="interconnects_posts",
            metadata={"hnsw:space": "cosine"}
        )
        
        documents = []
        metadatas = []
        ids = []
        chunk_id = 0
        
        print("Indexing posts...")
        
        for year_dir in sorted(public_path.iterdir()):
            if not year_dir.is_dir():
                continue
                
            print(f"Processing {year_dir.name}...")
            
            for post_file in sorted(year_dir.glob("*.md")):
                frontmatter, content = self.extract_frontmatter_and_content(post_file)
                
                if not content:
                    continue
                
                # Extract metadata
                title = frontmatter.get('title', post_file.stem)
                date = frontmatter.get('date', '')
                post_id = frontmatter.get('post_id', '')
                url = frontmatter.get('canonical_url', '')
                
                # Create chunks
                chunks = self.chunk_text(content)
                
                for i, chunk in enumerate(chunks):
                    documents.append(chunk)
                    metadatas.append({
                        'title': title,
                        'date': str(date),
                        'post_id': post_id,
                        'url': url,
                        'file_path': str(post_file),
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'year': year_dir.name
                    })
                    ids.append(f"{post_file.stem}_chunk_{i}")
                    chunk_id += 1
        
        print(f"Adding {len(documents)} chunks to vector database...")
        
        # Add documents in batches to avoid memory issues
        batch_size = 100
        for i in range(0, len(documents), batch_size):
            batch_docs = documents[i:i+batch_size]
            batch_metas = metadatas[i:i+batch_size]
            batch_ids = ids[i:i+batch_size]
            
            self.collection.add(
                documents=batch_docs,
                metadatas=batch_metas,
                ids=batch_ids
            )
            
            print(f"Processed {min(i+batch_size, len(documents))}/{len(documents)} chunks")
        
        print(f"Indexing complete! Added {len(documents)} chunks from posts.")
    
    def search(self, query: str, n_results: int = 10, year_filter: str = None) -> List[Dict]:
        """
        Search for posts using semantic similarity.
        
        Args:
            query: Search query
            n_results: Number of results to return
            year_filter: Optional year to filter by (e.g., "2024")
        
        Returns:
            List of search results with metadata
        """
        where_clause = {}
        if year_filter:
            where_clause["year"] = year_filter
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_clause if where_clause else None
        )
        
        formatted_results = []
        for i, (doc, metadata, distance) in enumerate(zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )):
            formatted_results.append({
                'rank': i + 1,
                'content': doc,
                'title': metadata['title'],
                'date': metadata['date'],
                'url': metadata['url'],
                'similarity_score': 1 - distance,  # Convert distance to similarity
                'chunk_info': f"{metadata['chunk_index'] + 1}/{metadata['total_chunks']}",
                'year': metadata['year']
            })
        
        return formatted_results
    
    def get_stats(self) -> Dict:
        """Get statistics about the indexed content."""
        count = self.collection.count()
        
        # Get unique posts count
        all_metadata = self.collection.get()['metadatas']
        unique_posts = len(set(meta['post_id'] for meta in all_metadata if meta['post_id']))
        
        # Get year distribution
        year_counts = {}
        for meta in all_metadata:
            year = meta.get('year', 'unknown')
            year_counts[year] = year_counts.get(year, 0) + 1
        
        return {
            'total_chunks': count,
            'unique_posts': unique_posts,
            'year_distribution': year_counts
        }


def main():
    """Command line interface for the search system."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Semantic search for Interconnects posts")
    parser.add_argument('--index', action='store_true', help='Index all posts')
    parser.add_argument('--search', type=str, help='Search query')
    parser.add_argument('--year', type=str, help='Filter by year')
    parser.add_argument('--results', type=int, default=5, help='Number of results (default: 5)')
    parser.add_argument('--stats', action='store_true', help='Show database statistics')
    
    args = parser.parse_args()
    
    search_system = InterconnectsSearch()
    
    if args.index:
        search_system.index_posts()
    elif args.search:
        results = search_system.search(args.search, args.results, args.year)
        
        print(f"\nSearch results for: '{args.search}'")
        if args.year:
            print(f"Filtered by year: {args.year}")
        print("=" * 80)
        
        for result in results:
            print(f"\n{result['rank']}. {result['title']} ({result['date']})")
            print(f"   Similarity: {result['similarity_score']:.3f} | Chunk: {result['chunk_info']}")
            print(f"   URL: {result['url']}")
            print(f"   Preview: {result['content'][:200]}...")
            print("-" * 80)
    elif args.stats:
        stats = search_system.get_stats()
        print("\nDatabase Statistics:")
        print(f"Total chunks: {stats['total_chunks']}")
        print(f"Unique posts: {stats['unique_posts']}")
        print("\nYear distribution:")
        for year, count in sorted(stats['year_distribution'].items()):
            print(f"  {year}: {count} chunks")
    else:
        print("Use --index to index posts, --search 'query' to search, or --stats for statistics")


if __name__ == "__main__":
    main()