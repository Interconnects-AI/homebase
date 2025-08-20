#!/usr/bin/env python3
"""
Utility to ensure Chroma database is indexed before using search tools.
This script checks if the database exists and indexes posts if needed.
"""

import sys
from pathlib import Path
from chroma_search import InterconnectsSearch

def ensure_indexed():
    """Ensure posts are indexed in Chroma database."""
    search = InterconnectsSearch()
    
    try:
        stats = search.get_stats()
        if stats['total_chunks'] > 0:
            print(f"Database already indexed: {stats['total_chunks']} chunks from {stats['unique_posts']} posts")
            return True
    except:
        print("Database not found, indexing posts...")
    
    # Check if public directory exists
    public_dir = Path("./public")
    if not public_dir.exists():
        print("ERROR: public/ directory not found. Make sure you're in the interconnects-home directory.")
        return False
    
    # Index posts
    try:
        search.index_posts()
        stats = search.get_stats()
        print(f"Indexing complete: {stats['total_chunks']} chunks from {stats['unique_posts']} posts")
        return True
    except Exception as e:
        print(f"ERROR: Failed to index posts: {e}")
        return False

if __name__ == "__main__":
    success = ensure_indexed()
    sys.exit(0 if success else 1)