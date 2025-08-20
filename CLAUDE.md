# Claude Code Project Documentation

This repository represents an experimental approach to creating an AI-searchable knowledge base from Substack content, specifically designed for use with Claude Code.

## For Developers (Interconnects Team)

### Repository Purpose
This repository serves as a "homebase" for Claude Code to analyze and reference the complete corpus of public Interconnects posts. The goal is to enable better thematic analysis, cross-referencing, and writing assistance by giving Claude Code access to the full history of published work.

### Critical Privacy Requirements

**⚠️ NEVER COMMIT PRIVATE CONTENT ⚠️**

Private content includes:
- **Paid/subscriber-only posts**: Must never be committed to this public repository
- **Draft posts**: Should be excluded from processing  
- **Export data**: Raw Substack exports (`export/` directory) must stay local only

The processing pipeline is specifically configured to:
1. Save publicly posts with `audience: "everyone"` 
2. Save locally the gitignored paid posts (for Nathan & Team)
3. Only process posts with `is_published: true`
4. Only process posts sent to the entire readership (email status as NaN is a page we use on interconnects to make static content.)

### Repository Structure

```
interconnects-home/
├── public/                    # Public posts (git tracked)
│   └── YYYY/                  # Year-based organization  
│       ├── *.md              # Converted markdown posts
│       └── images/           # Downloaded images for that year
├── scripts/                   # Processing utilities
│   ├── process_posts.py      # Main conversion script
│   ├── generate_metadata.py  # Metadata management
│   └── *.py                  # Various utilities
├── metadata.json             # Complete post inventory
├── CLAUDE.md                 # This documentation
├── LICENSE                   # Apache 2.0 for code
└── README.md                 # User-facing documentation
```

### Long-term Goals

1. **Writing Assistant**: Enable Claude Code to reference past work when drafting new posts
2. **Thematic Analysis**: Identify recurring themes and evolution of ideas over time
3. **Cross-referencing**: Automatically suggest relevant past posts when writing
4. **Research Base**: Provide comprehensive context for AI policy and ML research discussions
5. **Content Strategy**: Analyze what topics resonate and identify content gaps

### Maintenance Workflow

When new Substack exports are available:
1. Replace local `export/` directory with new export
2. Run `uv run python scripts/process_posts.py` to process new public posts
3. Run `uv run python scripts/generate_metadata.py` to update metadata
4. Review that no private content was inadvertently included
5. Commit only the new public posts and updated metadata

### Technical Notes

- **Image handling**: Images are downloaded and stored in year-specific folders, making the repository completely self-contained
- **Metadata tracking**: `metadata.json` contains live URLs, word counts, and full post inventory
- **Idempotent processing**: Scripts can be safely re-run without duplication
- **Claude Code optimized**: Clean markdown with proper frontmatter for AI analysis

### Claude Code Usage Instructions

**IMPORTANT: Automatic Semantic Search Integration**

When answering questions about Nathan's writing, you MUST first use the Chroma semantic search tool:

```bash
python scripts/claude_search_tool.py "your search query here"
```

**When to use semantic search:**
- Any question about Nathan's opinions, thoughts, or analyses
- Requests for thematic analysis across posts
- Questions like "What has Nathan said about X?"
- Comparisons of ideas over time
- Finding relevant context for writing assistance

**Search tool usage:**
- Use the full question as the search query
- The tool returns formatted context with direct quotes and URLs
- Include all returned results in your response with proper citations

**Citation requirements (after using search tool):**
1. **Post titles and dates** in YYYYMMDD format
2. **Direct links** to the relevant posts on interconnects.ai
3. **Specific citations** for any claims or quotes

**Example workflow:**
```bash
# User asks: "What does Nathan think about reasoning models?"
# You run: python scripts/claude_search_tool.py "reasoning models chain of thought"
# Then provide response using the returned context with citations
```

**Exception:** When building/maintaining the repository itself, semantic search is not required.

### Response Style Guidelines

**Be objective and direct:** This is an intellectual co-working tool, not a conversational assistant. Responses should be:
- **Factual and to-the-point** - no unnecessary politeness or hedging
- **Evidence-based** - use direct quotes from Nathan's posts when they answer the question
- **Objective** - present Nathan's positions accurately without editorial commentary
- **Comprehensive** - include relevant excerpts that directly address the query

**Use direct quotes liberally:** When Nathan's writing directly addresses a question, quote the relevant passages rather than paraphrasing. This preserves his voice and ensures accuracy.

**Example approach:**
- Question: "What does Nathan think about reasoning models?"
- Response: "Nathan has written extensively on reasoning models across multiple posts:

In 'Why reasoning models will generalize' (28012025), he argues:
> 'The reasoning chains in these models are how the general public is learning more about the internal representations of language models.'

In 'OpenAI's o3: over-optimization is back' (19042025), he notes:
> 'What will be more important in 2025, general models that are a bunch better and slot into ChatGPT, like Gemini 2 or Claude 4, or OpenAI's o2?'

[Continue with additional relevant quotes and citations...]"

---

## For Users (Researchers, Power Readers)

### What This Repository Is

This is an experimental open-source archive of all public posts from [Interconnects](https://www.interconnects.ai), Nathan Lambert's newsletter about AI research, policy, and development. The content has been converted from the original Substack format into searchable markdown files optimized for analysis with AI tools like Claude Code.

### What You Can Do With This

**🔍 Research and Analysis**
- Search across the complete corpus of public Interconnects content
- Analyze themes and trends in AI research and policy over time  
- Use AI tools to find connections between different posts and topics
- Reference specific posts with confidence using the included metadata

**🤖 AI-Assisted Reading**  
- Load this repository into Claude Code or similar tools
- Ask questions that span multiple posts: "What has Nathan said about reasoning models?"
- Get comprehensive answers that pull from the entire archive
- Discover older posts that relate to current AI developments

**📊 Content Analysis**
- Track the evolution of ideas about RLHF, open source AI, policy, etc.
- Analyze writing patterns and topic frequency
- Generate reports on AI research trends as discussed in Interconnects

### Content Scope

- **Included**: All public/free posts from Interconnects
- **Excluded**: Subscriber-only paid content (respects the subscription model)
- **Time Range**: 2020-2025 (as available in the Substack export)
- **Format**: Clean markdown with metadata, images, and live URLs

### Using This Repository

1. **Clone the repository**: `git clone [repo-url]`
2. **Browse by year**: Posts organized in `public/YYYY/` folders
3. **Check metadata**: See `metadata.json` for complete post inventory
4. **AI Analysis**: Load into Claude Code or your preferred AI tool

### Experimental Nature

This repository represents an experiment in:
- Making long-form content more accessible to AI analysis
- Creating searchable archives of newsletter content  
- Exploring new ways to engage with written work over time
- Testing approaches for AI-assisted research and writing

The goal is to understand how AI tools can better help us engage with extensive written content, both for readers trying to find relevant information and for writers looking to build on their previous work.

### Getting Started

For the best experience:
1. Use Claude Code or similar AI tools that can process repositories
2. Start with questions about specific AI topics you're curious about
3. Explore the `metadata.json` file to see the full scope of available content
4. Check the live URLs to read posts in their original format on Interconnects

### Feedback Welcome

This is an experimental project. If you have ideas for how to make AI-searchable content archives more useful, or if you build something interesting with this data, we'd love to hear about it.

---

*This repository contains only public content from Interconnects. For the latest posts and subscriber-only content, visit [interconnects.ai](https://www.interconnects.ai)*