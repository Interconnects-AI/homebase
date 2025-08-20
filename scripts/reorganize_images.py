#!/usr/bin/env python3
"""
Reorganize images into year-specific folders and update markdown references.
"""

import re
import shutil
from pathlib import Path

def reorganize_images():
    """Move images to year-specific folders and update markdown files."""
    
    images_dir = Path("images")
    if not images_dir.exists():
        print("No images directory found")
        return
    
    # Map post_id to year and visibility
    post_info = {}
    
    # Scan all markdown files to determine year/visibility
    for visibility in ["public", "private"]:
        base_dir = Path(visibility)
        if base_dir.exists():
            for year_dir in base_dir.iterdir():
                if year_dir.is_dir() and year_dir.name.isdigit():
                    year = year_dir.name
                    for md_file in year_dir.glob("*.md"):
                        # Extract post_id from markdown files
                        try:
                            content = md_file.read_text()
                            # Look for post_id in frontmatter
                            match = re.search(r'post_id: (.+)', content)
                            if match:
                                post_id = match.group(1).strip()
                                post_info[post_id] = {
                                    'year': year,
                                    'visibility': visibility,
                                    'md_file': md_file
                                }
                        except Exception as e:
                            print(f"Error reading {md_file}: {e}")
    
    # Move images and update references
    moved_count = 0
    for image_file in images_dir.glob("*.png"):
        filename = image_file.name
        
        # Extract post_id from image filename (before first underscore)
        post_id_match = re.match(r'([^_]+\.[^_]+)', filename)
        if not post_id_match:
            print(f"Could not extract post_id from {filename}")
            continue
            
        post_id = post_id_match.group(1)
        
        # Find matching post info
        if post_id not in post_info:
            print(f"No post info found for {post_id} (image: {filename})")
            continue
        
        info = post_info[post_id]
        year = info['year']
        visibility = info['visibility']
        
        # Create target directory and move image
        target_dir = Path(visibility) / year / "images"
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / filename
        
        print(f"Moving {filename} -> {target_file}")
        shutil.move(image_file, target_file)
        
        # Update markdown file to use relative path
        md_file = info['md_file']
        try:
            content = md_file.read_text()
            old_ref = f"images/{filename}"
            new_ref = f"images/{filename}"  # Relative to the markdown file
            
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                md_file.write_text(content)
                print(f"  Updated reference in {md_file}")
            
        except Exception as e:
            print(f"  Error updating {md_file}: {e}")
        
        moved_count += 1
    
    # Remove empty images directory
    if images_dir.exists() and not list(images_dir.iterdir()):
        images_dir.rmdir()
        print("Removed empty images directory")
    
    print(f"\nMoved {moved_count} images to year-specific folders")

if __name__ == "__main__":
    reorganize_images()