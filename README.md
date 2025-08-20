# Interconnects Archive

This repository contains scripts to process Substack export data and convert it into organized markdown files for Claude Code analysis and reference.

## Structure

- `public/YYYY/` - Public posts organized by year (git tracked)
  - `public/YYYY/images/` - Images for that year's public posts
- `private/YYYY/` - Paid posts organized by year (git ignored, local only)  
  - `private/YYYY/images/` - Images for that year's private posts
- `scripts/` - Processing and utility scripts
- `export/` - Original Substack export data (git ignored)
- `metadata.json` - Current posts metadata for easy updates

## Usage

### Setup
```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### Processing Posts
```bash
# Process all posts (this may take time due to image downloads)
uv run python scripts/process_posts.py

# Generate metadata for current posts
uv run python scripts/generate_metadata.py

# Quick statistics 
uv run python scripts/quick_stats.py

# Detailed analysis
uv run python scripts/stats.py
```

### Adding New Posts
When you get a new Substack export:

1. Replace `export/` directory with new export data
2. Run `uv run python scripts/process_posts.py` to process any new posts
3. Run `uv run python scripts/generate_metadata.py` to update metadata
4. Commit the new posts to git

The scripts are designed to be idempotent - you can re-run them safely.

## Features

✅ **Clean conversion**: HTML to markdown using pandoc  
✅ **Smart organization**: Separates public vs paid posts by year  
✅ **Year-specific images**: Images organized in `YYYY/images/` folders and git-tracked  
✅ **Rich metadata**: Preserves dates, types, audience info in frontmatter  
✅ **Live URL mapping**: Generates interconnects.ai links for each post  
✅ **Metadata tracking**: JSON file with all post info for easy updates  
✅ **Claude Code ready**: Optimized for AI analysis and search

## Post Metadata Format

Each post includes structured frontmatter:
```yaml
---
title: "Post Title"
subtitle: "Post subtitle if any"
date: YYYY-MM-DD
type: newsletter|podcast
audience: everyone|only_paid
visibility: public|private
post_id: original.slug.id
email_sent_at: ISO timestamp
---
```

## Metadata System

The `metadata.json` file contains:
- **Summary stats**: Total posts, word counts, years covered
- **All posts**: Full metadata for each post including live URLs
- **Recent posts**: Last 10 posts for quick reference
- **Stats**: Breakdown by year and post type

This makes it easy to:
- Find posts by title, date, or type
- Track word count and posting frequency
- Generate analytics and reports
- Quickly identify new posts when updating

## Repository Stats

Run `uv run python scripts/quick_stats.py` for current counts.