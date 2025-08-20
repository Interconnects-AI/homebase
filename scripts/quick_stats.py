#!/usr/bin/env python3
"""Quick stats for the repository."""

from pathlib import Path

def quick_stats():
    public_count = len(list(Path("public").rglob("*.md")))
    private_count = len(list(Path("private").rglob("*.md")))
    image_count = len(list(Path("images").glob("*.png"))) if Path("images").exists() else 0
    
    print(f"📄 Public posts: {public_count}")
    print(f"🔒 Private posts: {private_count}")  
    print(f"🖼️ Downloaded images: {image_count}")
    print(f"📦 Total posts: {public_count + private_count}")
    
    # Year breakdown
    print("\n📅 Posts by year:")
    years = {}
    for visibility in ["public", "private"]:
        if Path(visibility).exists():
            for year_dir in Path(visibility).iterdir():
                if year_dir.is_dir():
                    year = year_dir.name
                    count = len(list(year_dir.glob("*.md")))
                    if count > 0:
                        if year not in years:
                            years[year] = {"public": 0, "private": 0}
                        years[year][visibility] = count
    
    for year in sorted(years.keys()):
        public = years[year]["public"]
        private = years[year]["private"]
        total = public + private
        print(f"  {year}: {total} total ({public} public, {private} private)")

if __name__ == "__main__":
    quick_stats()