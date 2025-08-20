#!/usr/bin/env python3
"""
Generate and maintain metadata about current posts for easy updates and reference.
"""

import json
from datetime import datetime
from pathlib import Path
import frontmatter

def extract_live_url(post_id: str, title: str) -> str:
    """Generate likely live URL from post metadata."""
    # Extract slug from post_id (everything after the first dot)
    if '.' in post_id:
        slug = post_id.split('.', 1)[1]
        return f"https://www.interconnects.ai/p/{slug}"
    else:
        # Fallback: create slug from title
        slug = title.lower().replace(' ', '-').replace(':', '').replace('?', '').replace('!', '')
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        return f"https://www.interconnects.ai/p/{slug}"

def scan_posts():
    """Scan all processed posts and generate metadata."""
    posts = []
    
    for visibility in ["public", "private"]:
        base_dir = Path(visibility)
        if not base_dir.exists():
            continue
            
        for year_dir in base_dir.iterdir():
            if not year_dir.is_dir() or not year_dir.name.isdigit():
                continue
                
            year = year_dir.name
            for md_file in year_dir.glob("*.md"):
                try:
                    # Parse frontmatter
                    with open(md_file, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                    
                    meta = post.metadata
                    
                    # Extract key information
                    post_data = {
                        "title": meta.get('title', 'Untitled'),
                        "subtitle": meta.get('subtitle', ''),
                        "date": meta.get('date', ''),
                        "year": year,
                        "type": meta.get('type', 'newsletter'),
                        "audience": meta.get('audience', 'everyone'), 
                        "visibility": meta.get('visibility', visibility),
                        "post_id": meta.get('post_id', ''),
                        "email_sent_at": meta.get('email_sent_at', ''),
                        "live_url": extract_live_url(meta.get('post_id', ''), meta.get('title', '')),
                        "local_file": str(md_file),
                        "word_count": len(post.content.split()),
                        "tags": [],  # TODO: Add tagging system
                        "processed_at": datetime.now().isoformat()
                    }
                    
                    posts.append(post_data)
                    
                except Exception as e:
                    print(f"Error processing {md_file}: {e}")
    
    # Sort by date (newest first)
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    return posts

def generate_metadata():
    """Generate comprehensive metadata file."""
    print("Scanning processed posts...")
    posts = scan_posts()
    
    # Generate summary statistics
    total_posts = len(posts)
    public_posts = len([p for p in posts if p['visibility'] == 'public'])
    private_posts = len([p for p in posts if p['visibility'] == 'private'])
    
    # Posts by year
    year_stats = {}
    for post in posts:
        year = post['year']
        if year not in year_stats:
            year_stats[year] = {"public": 0, "private": 0, "total": 0}
        year_stats[year][post['visibility']] += 1
        year_stats[year]["total"] += 1
    
    # Posts by type
    type_stats = {}
    for post in posts:
        post_type = post['type']
        if post_type not in type_stats:
            type_stats[post_type] = {"public": 0, "private": 0, "total": 0}
        type_stats[post_type][post['visibility']] += 1
        type_stats[post_type]["total"] += 1
    
    # Recent posts (last 10)
    recent_posts = posts[:10]
    
    # Total word count
    total_words = sum(p['word_count'] for p in posts)
    
    metadata = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_posts": total_posts,
            "public_posts": public_posts,
            "private_posts": private_posts,
            "total_words": total_words,
            "years_covered": sorted(year_stats.keys())
        },
        "stats": {
            "by_year": year_stats,
            "by_type": type_stats
        },
        "recent_posts": recent_posts,
        "all_posts": posts
    }
    
    # Save metadata
    metadata_file = Path("metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2, default=str)
    
    print(f"Generated metadata for {total_posts} posts")
    print(f"  Public: {public_posts}")
    print(f"  Private: {private_posts}")
    print(f"  Total words: {total_words:,}")
    print(f"  Years: {', '.join(sorted(year_stats.keys()))}")
    print(f"  Saved to: {metadata_file}")
    
    return metadata

def find_new_posts():
    """Compare current posts with metadata to find new ones."""
    metadata_file = Path("metadata.json")
    if not metadata_file.exists():
        print("No existing metadata found. Run generate_metadata() first.")
        return []
    
    with open(metadata_file) as f:
        old_metadata = json.load(f)
    
    old_posts = {p['post_id']: p for p in old_metadata['all_posts']}
    current_posts = scan_posts()
    
    new_posts = []
    for post in current_posts:
        if post['post_id'] not in old_posts:
            new_posts.append(post)
    
    return new_posts

if __name__ == "__main__":
    generate_metadata()