#!/usr/bin/env python3
"""
Generate statistics about the processed posts.
"""

import json
from collections import defaultdict
from pathlib import Path
import frontmatter

def analyze_posts():
    """Analyze all processed posts and generate statistics."""
    
    public_dir = Path("public/posts")
    private_dir = Path("private/posts")
    
    stats = {
        "total_posts": 0,
        "public_posts": 0,
        "private_posts": 0,
        "by_year": defaultdict(lambda: {"public": 0, "private": 0}),
        "by_type": defaultdict(lambda: {"public": 0, "private": 0}),
        "recent_posts": [],
    }
    
    def process_directory(directory, visibility):
        """Process posts in a directory."""
        for md_file in directory.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                # Extract metadata
                year = post.metadata.get('date', '').split('-')[0] if post.metadata.get('date') else 'unknown'
                post_type = post.metadata.get('type', 'unknown')
                title = post.metadata.get('title', 'Untitled')
                date = post.metadata.get('date', '')
                
                # Update stats
                stats["total_posts"] += 1
                stats[f"{visibility}_posts"] += 1
                stats["by_year"][year][visibility] += 1
                stats["by_type"][post_type][visibility] += 1
                
                # Add to recent posts
                stats["recent_posts"].append({
                    "title": title,
                    "date": date,
                    "type": post_type,
                    "visibility": visibility,
                    "file": str(md_file)
                })
                
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
    
    # Process both directories
    if public_dir.exists():
        process_directory(public_dir, "public")
    if private_dir.exists():
        process_directory(private_dir, "private")
    
    # Sort recent posts by date (descending)
    stats["recent_posts"].sort(key=lambda x: x.get("date", ""), reverse=True)
    stats["recent_posts"] = stats["recent_posts"][:10]  # Keep only 10 most recent
    
    return stats

def print_stats(stats):
    """Print formatted statistics."""
    print("=== INTERCONNECTS ARCHIVE STATISTICS ===\\n")
    
    print(f"Total Posts: {stats['total_posts']}")
    print(f"Public Posts: {stats['public_posts']}")
    print(f"Private Posts: {stats['private_posts']}")
    print()
    
    print("Posts by Year:")
    years = sorted(stats['by_year'].keys())
    for year in years:
        if year != 'unknown':
            public = stats['by_year'][year]['public']
            private = stats['by_year'][year]['private']
            total = public + private
            print(f"  {year}: {total} total ({public} public, {private} private)")
    print()
    
    print("Posts by Type:")
    for post_type in sorted(stats['by_type'].keys()):
        public = stats['by_type'][post_type]['public']
        private = stats['by_type'][post_type]['private']
        total = public + private
        print(f"  {post_type}: {total} total ({public} public, {private} private)")
    print()
    
    print("Most Recent Posts:")
    for post in stats['recent_posts']:
        visibility_emoji = "🔓" if post['visibility'] == 'public' else "🔒"
        print(f"  {visibility_emoji} {post['date']} - {post['title']} ({post['type']})")

def main():
    try:
        stats = analyze_posts()
        print_stats(stats)
        
        # Save stats to JSON
        with open("stats.json", "w") as f:
            json.dump(stats, f, indent=2, default=str)
        print(f"\\nDetailed statistics saved to stats.json")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()