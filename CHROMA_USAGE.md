# Semantic Search with Chroma

This integration adds vector-based semantic search to the Interconnects archive using Chroma vector database.

## Setup

```bash
# Install additional dependencies
pip install -r requirements-chroma.txt

# Or with uv
uv add chromadb sentence-transformers tiktoken
```

## Usage

### Index all posts
```bash
python scripts/chroma_search.py --index
```

### Search semantically
```bash
# Basic search
python scripts/chroma_search.py --search "reasoning models and chain of thought"

# Filter by year
python scripts/chroma_search.py --search "open source AI" --year 2024

# Get more results
python scripts/chroma_search.py --search "RLHF alignment" --results 10
```

### Get statistics
```bash
python scripts/chroma_search.py --stats
```

## Example Searches

**Conceptual queries that work well:**
- "reasoning models and their limitations"
- "open source vs closed AI development"
- "AI safety and alignment concerns"
- "transformer architecture innovations"
- "policy implications of AI capabilities"

**Time-based analysis:**
- `--year 2024` to see recent discussions
- `--year 2023` for historical perspective

## How It Works

1. **Chunking**: Posts are split into ~500 token chunks with 50 token overlap
2. **Embeddings**: Each chunk gets embedded using sentence-transformers
3. **Storage**: Chroma stores embeddings with metadata (title, date, URL, etc.)
4. **Search**: Semantic similarity matching using cosine distance

## Benefits Over Text Search

- **Conceptual matching**: Find posts about "model reasoning" even if they use different terms
- **Cross-post connections**: Discover related ideas across different time periods
- **Better retrieval**: Rank results by semantic relevance, not just keyword frequency
- **Research assistance**: "What has Nathan said about X over time?"

## Database Location

The Chroma database is stored in `./chroma_db/` and is gitignored to avoid large binary files in the repository.