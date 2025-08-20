#!/usr/bin/env python3
"""
Claude Code integration for semantic search over Interconnects posts.
This tool automatically uses Chroma to answer questions about Nathan's writing.
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Optional
from chroma_search import InterconnectsSearch


class ClaudeSearchTool:
    def __init__(self):
        """Initialize the search tool for Claude Code integration."""
        self.search = InterconnectsSearch()
        self.ensure_indexed()
    
    def ensure_indexed(self):
        """Ensure posts are indexed, or provide helpful error message."""
        try:
            stats = self.search.get_stats()
            if stats['total_chunks'] == 0:
                print("ERROR: No posts indexed. Run: python scripts/chroma_search.py --index", file=sys.stderr)
                sys.exit(1)
        except Exception as e:
            print(f"ERROR: Chroma database not found. Run: python scripts/chroma_search.py --index", file=sys.stderr)
            sys.exit(1)
    
    def search_posts(self, query: str, max_results: int = 5, year_filter: Optional[str] = None) -> Dict:
        """
        Search Nathan's posts and return structured results for Claude.
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            year_filter: Optional year filter (e.g., "2024")
        
        Returns:
            Structured search results with context for Claude
        """
        try:
            results = self.search.search(query, n_results=max_results, year_filter=year_filter)
            
            # Format results for Claude consumption
            formatted_results = {
                "query": query,
                "total_results": len(results),
                "year_filter": year_filter,
                "results": []
            }
            
            for result in results:
                formatted_results["results"].append({
                    "title": result['title'],
                    "date": result['date'],
                    "url": result['url'],
                    "content_preview": result['content'],
                    "similarity_score": round(result['similarity_score'], 3),
                    "chunk_info": result['chunk_info'],
                    "year": result['year']
                })
            
            return formatted_results
            
        except Exception as e:
            return {"error": f"Search failed: {str(e)}", "query": query}
    
    def get_post_context(self, topic: str, max_results: int = 8) -> str:
        """
        Get comprehensive context about a topic from Nathan's posts.
        Returns formatted text suitable for Claude to reference.
        """
        results = self.search_posts(topic, max_results=max_results)
        
        if "error" in results:
            return f"Error searching posts: {results['error']}"
        
        if not results["results"]:
            return f"No posts found matching: '{topic}'"
        
        # Format for Claude reference
        context = f"## Search Results for '{topic}'\n\n"
        context += f"Found {results['total_results']} relevant sections from Nathan's posts:\n\n"
        
        for i, result in enumerate(results["results"], 1):
            context += f"### {i}. {result['title']} ({result['date']})\n"
            context += f"**Relevance:** {result['similarity_score']}\n"
            context += f"**URL:** {result['url']}\n\n"
            context += f"{result['content_preview']}\n\n"
            context += "---\n\n"
        
        return context
    
    def answer_question_about_posts(self, question: str) -> str:
        """
        Answer a question about Nathan's posts using semantic search.
        This is the main method Claude should use.
        """
        # Extract key concepts from the question for better search
        search_query = question.lower()
        
        # Get relevant context
        context = self.get_post_context(question, max_results=6)
        
        if context.startswith("Error") or context.startswith("No posts"):
            return context
        
        # Add instruction for Claude
        response = f"""Based on Nathan's writing in Interconnects, here's what I found about: "{question}"

{context}

**Instructions for Claude:** Use the above search results to provide a comprehensive answer about Nathan's thoughts on this topic. Include direct quotes where relevant and cite the specific posts with their URLs."""
        
        return response


def main():
    """Command line interface for Claude integration."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Search Nathan's posts for Claude Code")
    parser.add_argument('query', help='Search query or question')
    parser.add_argument('--year', type=str, help='Filter by year')
    parser.add_argument('--results', type=int, default=5, help='Number of results')
    parser.add_argument('--raw', action='store_true', help='Return raw JSON instead of formatted text')
    
    args = parser.parse_args()
    
    tool = ClaudeSearchTool()
    
    if args.raw:
        # Return JSON for programmatic use
        results = tool.search_posts(args.query, args.results, args.year)
        print(json.dumps(results, indent=2))
    else:
        # Return formatted context for Claude
        response = tool.answer_question_about_posts(args.query)
        print(response)


if __name__ == "__main__":
    main()