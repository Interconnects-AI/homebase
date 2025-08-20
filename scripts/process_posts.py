#!/usr/bin/env python3
"""
Process Substack export data into organized markdown files.

This script:
1. Reads posts.csv to get metadata
2. Processes HTML files and converts to markdown
3. Organizes by year and public/private status
4. Preserves metadata in frontmatter
"""

import csv
import os
import re
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

import pandas as pd
import pypandoc
from bs4 import BeautifulSoup


class SubstackProcessor:
    def __init__(self, export_dir: str = "export", output_base: str = "."):
        self.export_dir = Path(export_dir)
        self.output_base = Path(output_base)
        self.posts_csv = self.export_dir / "posts.csv"
        self.posts_dir = self.export_dir / "posts"
        
        # Ensure output directories exist
        for visibility in ["public", "private"]:
            for year in range(2020, 2026):
                (self.output_base / visibility / str(year)).mkdir(parents=True, exist_ok=True)
        
        # Images will be stored in year-specific folders
    
    def load_metadata(self) -> pd.DataFrame:
        """Load and process the posts.csv metadata."""
        df = pd.read_csv(self.posts_csv)
        
        # Convert post_date to datetime
        df['post_date'] = pd.to_datetime(df['post_date'])
        
        # Filter only published posts with valid dates
        df = df[df['is_published'] == True].copy()
        df = df.dropna(subset=['post_date'])
        
        # Extract year
        df['year'] = df['post_date'].dt.year
        
        # Determine visibility
        df['visibility'] = df['audience'].map({
            'everyone': 'public',
            'only_paid': 'private'
        })
        
        return df
    
    def find_html_file(self, post_id: str) -> Optional[Path]:
        """Find the HTML file for a given post ID."""
        # The post_id is actually the full slug, so just add .html
        html_file = self.posts_dir / f"{post_id}.html"
        if html_file.exists():
            return html_file
        return None
    
    def download_image(self, img_url: str, post_id: str, visibility: str, year: str) -> Optional[str]:
        """Download image and return local path."""
        try:
            # Parse image URL to get filename
            parsed = urlparse(img_url)
            if 'substack' not in img_url.lower():
                return None
                
            # Extract image ID from URL
            if 'images/' in img_url:
                img_id = img_url.split('images/')[-1].split('_')[0]
            else:
                return None
                
            # Generate local filename
            img_filename = f"{post_id}_{img_id}.png"
            
            # Year-specific image directory
            img_dir = self.output_base / visibility / year / "images"
            img_dir.mkdir(parents=True, exist_ok=True)
            img_path = img_dir / img_filename
            
            # Download if not exists
            if not img_path.exists():
                response = requests.get(img_url, stream=True, timeout=10)
                response.raise_for_status()
                
                with open(img_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            
            return f"images/{img_filename}"
            
        except Exception as e:
            print(f"  Warning: Could not download image {img_url}: {e}")
            return None

    def clean_html_content(self, html_content: str, post_id: str, visibility: str, year: str) -> str:
        """Clean and prepare HTML content for conversion."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove subscription widgets and buttons
        for element in soup.find_all(['div', 'p'], class_=lambda x: x and 'subscription' in str(x).lower()):
            element.decompose()
        
        for element in soup.find_all(['p'], class_=lambda x: x and 'button-wrapper' in str(x).lower()):
            element.decompose()
            
        # Remove share buttons
        for element in soup.find_all('a', class_=lambda x: x and 'button' in str(x).lower()):
            element.decompose()
        
        # Clean up mention wraps but preserve the content
        for mention in soup.find_all('span', class_='mention-wrap'):
            if mention.string:
                mention.replace_with(mention.string)
            else:
                mention.unwrap()
        
        # Clean up complex image structures - replace with simple img tags
        for captioned_container in soup.find_all('div', class_='captioned-image-container'):
            # Find the main image
            img_tag = captioned_container.find('img')
            if img_tag and img_tag.get('src'):
                img_src = img_tag.get('src')
                
                # Try to download image for public posts
                local_path = self.download_image(img_src, post_id, visibility, year)
                
                # Create clean image tag
                new_img = soup.new_tag('img')
                new_img['src'] = local_path if local_path else img_src
                new_img['alt'] = img_tag.get('alt', '')
                
                # Replace the entire complex structure with simple img
                captioned_container.replace_with(new_img)
        
        return str(soup)
    
    def convert_to_markdown(self, html_content: str, title: str, post_id: str, visibility: str, year: str) -> str:
        """Convert HTML content to markdown using pandoc."""
        try:
            # Clean the HTML first
            clean_html = self.clean_html_content(html_content, post_id, visibility, year)
            
            # Convert to markdown
            markdown = pypandoc.convert_text(
                clean_html, 
                'markdown',
                format='html',
                extra_args=['--wrap=none']
            )
            
            return markdown
        except Exception as e:
            print(f"Error converting {title}: {e}")
            return f"# {title}\\n\\nError converting content: {e}"
    
    def create_frontmatter(self, row: pd.Series) -> str:
        """Create YAML frontmatter for the post."""
        frontmatter = ["---"]
        
        # Basic metadata
        frontmatter.append(f"title: \"{row['title'] or 'Untitled'}\"")
        if pd.notna(row['subtitle']) and row['subtitle']:
            frontmatter.append(f"subtitle: \"{row['subtitle']}\"")
        
        frontmatter.append(f"date: {row['post_date'].strftime('%Y-%m-%d')}")
        frontmatter.append(f"type: {row['type']}")
        frontmatter.append(f"audience: {row['audience']}")
        frontmatter.append(f"visibility: {row['visibility']}")
        
        if pd.notna(row['podcast_url']) and row['podcast_url']:
            frontmatter.append(f"podcast_url: \"{row['podcast_url']}\"")
        
        # Technical metadata
        frontmatter.append(f"post_id: {row['post_id']}")
        frontmatter.append(f"email_sent_at: {row['email_sent_at']}")
        
        frontmatter.append("---")
        frontmatter.append("")
        
        return "\n".join(frontmatter)
    
    def get_output_path(self, row: pd.Series) -> Path:
        """Generate the output path for a post."""
        visibility = row['visibility']
        year = row['year']
        
        # Create a clean filename from title
        title = row['title'] or 'untitled'
        clean_title = re.sub(r'[^a-zA-Z0-9\\s-]', '', title)
        clean_title = re.sub(r'\\s+', '-', clean_title).lower()
        clean_title = clean_title[:50]  # Limit length
        
        # Add date prefix for better sorting
        date_prefix = row['post_date'].strftime('%Y-%m-%d')
        filename = f"{date_prefix}-{clean_title}.md"
        
        return self.output_base / visibility / str(year) / filename
    
    def process_single_post(self, row: pd.Series) -> bool:
        """Process a single post."""
        post_id = row['post_id']
        title = row['title'] or 'Untitled'
        
        # Find the HTML file
        html_file = self.find_html_file(post_id)
        if not html_file:
            print(f"No HTML file found for {post_id}: {title}")
            return False
        
        try:
            # Read HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Convert to markdown 
            visibility = row['visibility']
            year = str(row['year'])
            markdown_content = self.convert_to_markdown(html_content, title, post_id, visibility, year)
            
            # Create frontmatter
            frontmatter = self.create_frontmatter(row)
            
            # Combine frontmatter and content
            full_content = frontmatter + markdown_content
            
            # Write to output file
            output_path = self.get_output_path(row)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            print(f"✓ Processed: {title} -> {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error processing {title}: {e}")
            return False
    
    def process_all_posts(self):
        """Process all posts from the metadata."""
        print("Loading metadata...")
        df = self.load_metadata()
        
        print(f"Found {len(df)} published posts to process")
        
        # Count by visibility
        visibility_counts = df['visibility'].value_counts()
        print(f"Public posts: {visibility_counts.get('public', 0)}")
        print(f"Private posts: {visibility_counts.get('private', 0)}")
        
        # Count by year
        year_counts = df['year'].value_counts().sort_index()
        print("\\nPosts by year:")
        for year, count in year_counts.items():
            print(f"  {year}: {count}")
        
        print("\\nProcessing posts...")
        
        successful = 0
        failed = 0
        
        for _, row in df.iterrows():
            if self.process_single_post(row):
                successful += 1
            else:
                failed += 1
        
        print(f"\\nProcessing complete!")
        print(f"Successfully processed: {successful}")
        print(f"Failed: {failed}")
        print(f"Total: {successful + failed}")


def main():
    processor = SubstackProcessor()
    processor.process_all_posts()


if __name__ == "__main__":
    main()