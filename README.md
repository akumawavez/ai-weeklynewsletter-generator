# AI Weekly Newsletter Generator

An end-to-end pipeline that automatically curates, summarizes, and publishes a **weekly AI/LLM newsletter** for internal distribution. It ingests the [zenml/llmops-database](https://huggingface.co/datasets/zenml/llmops-database) dataset from Hugging Face, identifies the most relevant items for the current week, and uses an LLM to generate a polished, categorized newsletter in Markdown.

> Built as the "Automated AI Newsletter Generator" assignment for TelecomXYZ.

---

## Why this project

Keeping up with the AI/LLM space is hard — too many papers, blog posts, and product launches every week. This pipeline gives an organization a low-effort way to:

- **Stay ahead of trends** by surfacing the latest AI developments
- **Discover new use cases** that could inspire internal projects
- **Reduce information overload** through filtering and LLM summarization
- **Share knowledge** in a concise, digestible, weekly format

---

## Architecture

The pipeline is intentionally split into small, composable stages so each step can be tested, swapped, or scheduled independently.

```
 Hugging Face Dataset (zenml/llmops-database)
                │
                ▼
        [ 1. Ingest ]          ingest_data.py
                │               -> data/llmops_database.parquet
                │               -> data/llmops_database.db   (SQLite)
                │               -> data/llmops_documents.jsonl (RAG-ready)
                ▼
        [ 2. Filter ]          select fresh items for the current week
                │               (deduplicate against previous runs)
                ▼
        [ 3. Categorize ]      group items into:
                │               - Research Highlights
                │               - Industry News
                │               - Cool Use Cases
                ▼
        [ 4. Summarize ]       LLM-generated, newsletter-friendly summaries
                ▼
        [ 5. Render ]          Markdown newsletter (newsletter.md)
                ▼
        [ 6. Schedule ]        weekly run via GitHub Actions / cron
```

Each record from the dataset includes metadata such as `created_at`, `title`, `industry`, `company`, `source_url`, `application_tags`, `tools_tags`, `techniques_tags`, `short_summary`, and `full_summary`, which the pipeline uses for both filtering and prompt context.

---

## Project structure

```
ai-weeklynewsletter-generator/
├── ingest_data.py          # Stage 1: load HF dataset -> parquet + sqlite + jsonl
├── data/                   # Generated artifacts (gitignored)
│   ├── llmops_database.parquet
│   ├── llmops_database.db
│   └── llmops_documents.jsonl
├── .env.example            # Template for API keys / config
├── newsletter.md           # Sample generated newsletter
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Quickstart

### 1. Prerequisites

- Python 3.10+
- An API key for an LLM provider (e.g. OpenAI). An open-source / local model can be plugged in instead.

### 2. Clone & install

```bash
git clone https://github.com/<your-org>/ai-weeklynewsletter-generator.git
cd ai-weeklynewsletter-generator

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure environment

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

`.env` should contain at minimum:

```dotenv
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o-mini
NEWSLETTER_LOOKBACK_DAYS=7
```

### 4. Ingest the dataset

This downloads `zenml/llmops-database`, normalizes the columns, and writes the artifacts under `data/`:

```bash
python ingest_data.py
```

Output:

- `data/llmops_database.parquet` — queryable tabular version
- `data/llmops_database.db` — SQLite version (table `llmops_case_studies`)
- `data/llmops_documents.jsonl` — RAG-ready documents with rich `text` + `metadata`

### 5. Generate the newsletter *(coming next)*

```bash
python generate_newsletter.py --output newsletter.md
```

This reads the ingested data, selects items from the last `NEWSLETTER_LOOKBACK_DAYS`, groups them into sections, calls the LLM to summarize, and renders `newsletter.md`.

---

## How each stage works

### 1. Ingestion (`ingest_data.py`)

- Loads the Hugging Face dataset via `datasets.load_dataset`.
- Selects a stable subset of columns and coerces types (`created_at` -> datetime, `year` -> Int64).
- Normalizes list-typed tag fields (`application_tags`, `tools_tags`, `techniques_tags`, `extra_tags`) into clean comma-separated strings.
- Drops rows without a title.
- Builds a `rag_text` field per record — a single string with title, company, industry, tags, and summaries — so it can be embedded or fed into an LLM directly.
- Writes three formats: Parquet (analytics), SQLite (ad-hoc SQL), and JSONL (RAG / vector store ingestion).

### 2. Filtering & deduplication

- Items are filtered by `created_at` to include only the configured lookback window (default: last 7 days).
- A small state file (or table) tracks IDs already published in previous newsletters so the same case study is not featured twice.

### 3. Categorization

- Items are grouped into newsletter sections based on metadata:
  - **Research Highlights** — items tagged with research/technique-heavy tags.
  - **Industry News** — items grouped by `industry` / `company`.
  - **Cool Use Cases** — items with strong `application_tags`.
- Heuristics first; an LLM classifier can be added for borderline cases.

### 4. LLM summarization

- One concise prompt per section, with structured input (title, company, tags, short/full summary, source URL).
- The LLM is instructed to produce 2–3 sentence summaries with a consistent tone, plus a section-level intro line.
- Prompts and model choice live in a single config module so they are easy to tweak and version.

### 5. Rendering

- The newsletter is rendered as Markdown with:
  - A short introduction
  - Categorized sections with summaries and source links
  - A short closing section

A sample output is provided at `newsletter.md`.

---

## Automation

The pipeline is designed to run unattended on a weekly schedule.

**Option A — GitHub Actions (recommended):**

A workflow at `.github/workflows/weekly-newsletter.yml` runs every Monday at 07:00 UTC, executes `ingest_data.py` and `generate_newsletter.py`, and commits the new `newsletter.md` (or opens a PR) so it is reviewable before distribution.

**Option B — cron / Task Scheduler:**

```cron
0 7 * * 1  cd /path/to/ai-weeklynewsletter-generator && \
           .venv/bin/python ingest_data.py && \
           .venv/bin/python generate_newsletter.py --output newsletter.md
```

Re-runs are idempotent: ingestion overwrites the local snapshot, and newsletter generation skips items already published in earlier weeks.

---

## Design choices

- **Dataset-as-source-of-truth.** The HF dataset is treated as a read-only upstream feed. All transformations are local and reproducible.
- **Three storage formats on purpose.** Parquet for fast analytics, SQLite for portable ad-hoc queries during development, JSONL for downstream RAG / embedding pipelines.
- **`rag_text` precomputed at ingest.** Keeps the LLM stage simple and ensures the same context is used for retrieval and summarization.
- **Modular stages.** Each stage is a separate script/module with a clear input and output, so it can be tested or replaced (e.g. swap OpenAI for a local model) without touching the rest of the pipeline.
- **Markdown-first output.** Trivial to email, post to Slack/Teams, or publish to an internal wiki.

---

## Roadmap / bonus features

- [ ] Personalization — render different sections for *technical* vs *non-technical* readers.
- [ ] Quality evaluation — LLM-as-judge scoring (relevance, clarity, faithfulness) on each generated section.
- [ ] Vector-store-backed retrieval for "items similar to past hits".
- [ ] Slack / Teams / email delivery adapter.
- [ ] Configurable section taxonomy via YAML.

---

## Deliverables checklist

- [x] Source code for the pipeline
- [x] `README.md` with setup instructions and design explanation
- [ ] Sample generated `newsletter.md`
- [ ] `.env.example`
- [ ] Scheduled workflow (GitHub Actions)

---
