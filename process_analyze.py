import sqlite3
import json
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pandas as pd


DB_PATH = Path("data/llmops_database.db")
OUTPUT_DIR = Path("data")
PROCESSED_JSONL_PATH = OUTPUT_DIR / "processed_newsletter_items.jsonl"


SECTION_RULES = {
    "Research Highlights": [
        "research",
        "paper",
        "benchmark",
        "evaluation",
        "eval",
        "experiment",
        "model",
        "fine-tuning",
        "finetuning",
        "training",
        "rlhf",
        "rag evaluation",
    ],
    "Industry News": [
        "enterprise",
        "production",
        "deployment",
        "platform",
        "company",
        "customer",
        "business",
        "industry",
        "adoption",
        "scale",
        "infrastructure",
    ],
    "Cool Use Cases": [
        "agent",
        "workflow",
        "assistant",
        "copilot",
        "automation",
        "chatbot",
        "search",
        "support",
        "recommendation",
        "knowledge base",
        "use case",
    ],
    "Tools & Infrastructure": [
        "observability",
        "monitoring",
        "orchestration",
        "vector database",
        "embedding",
        "pipeline",
        "mlops",
        "llmops",
        "framework",
        "tool",
        "open source",
        "guardrails",
    ],
}


TRENDING_KEYWORDS = [
    "agent",
    "agents",
    "rag",
    "retrieval",
    "evaluation",
    "eval",
    "guardrails",
    "observability",
    "production",
    "workflow",
    "automation",
    "copilot",
    "multimodal",
    "embedding",
    "vector",
    "fine-tuning",
    "llmops",
    "open source",
]


def get_current_week_window():
    """
    Returns Monday 00:00 to Sunday 23:59 for the current local week.
    Uses system date.
    """
    today = datetime.now().date()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)

    return monday, sunday


def clean_text(value):
    if value is None:
        return ""

    if pd.isna(value):
        return ""

    return str(value).strip()


def normalize_whitespace(text):
    text = clean_text(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate_words(text, max_words=45):
    text = normalize_whitespace(text)
    words = text.split()

    if len(words) <= max_words:
        return text

    return " ".join(words[:max_words]).rstrip(".,;:") + "..."


def combined_search_text(row):
    fields = [
        "title",
        "company",
        "industry",
        "short_summary",
        "full_summary",
        "application_tags",
        "tools_tags",
        "techniques_tags",
        "extra_tags",
    ]

    return " ".join(clean_text(row.get(field, "")) for field in fields).lower()


def categorize_item(row):
    """
    Rule-based categorization.
    Good enough for GitHub Actions because it does not require an LLM key.
    """

    text = combined_search_text(row)

    section_scores = {}

    for section, keywords in SECTION_RULES.items():
        score = 0

        for keyword in keywords:
            if keyword.lower() in text:
                score += 1

        section_scores[section] = score

    best_section = max(section_scores, key=section_scores.get)

    if section_scores[best_section] == 0:
        return "Other Noteworthy Items"

    return best_section


def compute_trending_score(row, week_start, week_end):
    """
    Heuristic scoring for 'relevance/trending'.

    Since this dataset is not necessarily a live news feed, we infer relevance from:
    - whether created_at is from the current week
    - recent year
    - presence of high-interest LLMOps keywords
    - quality/completeness of summary
    - source URL availability
    """

    score = 0
    text = combined_search_text(row)

    # 1. Current week boost
    created_at = row.get("created_at")

    if created_at:
        try:
            created_date = pd.to_datetime(created_at, errors="coerce").date()

            if week_start <= created_date <= week_end:
                score += 40
            elif created_date >= week_start - timedelta(days=30):
                score += 20
            elif created_date >= week_start - timedelta(days=90):
                score += 10

        except Exception:
            pass

    # 2. Recent year boost
    year = row.get("year")

    try:
        year_int = int(year)
        current_year = datetime.now().year

        if year_int == current_year:
            score += 20
        elif year_int == current_year - 1:
            score += 12
        elif year_int >= current_year - 2:
            score += 6

    except Exception:
        pass

    # 3. Trending keyword boost
    for keyword in TRENDING_KEYWORDS:
        if keyword in text:
            score += 5

    # 4. Summary quality boost
    short_summary = clean_text(row.get("short_summary", ""))
    full_summary = clean_text(row.get("full_summary", ""))

    if len(short_summary.split()) >= 20:
        score += 8

    if len(full_summary.split()) >= 80:
        score += 8

    # 5. Source availability boost
    if clean_text(row.get("source_url", "")):
        score += 5

    # 6. Company and industry metadata boost
    if clean_text(row.get("company", "")):
        score += 3

    if clean_text(row.get("industry", "")):
        score += 3

    return score


def make_newsletter_summary(row):
    """
    Creates concise newsletter-friendly text without calling an LLM.
    You can later replace this with OpenAI/Anthropic if needed.
    """

    title = clean_text(row.get("title", ""))
    company = clean_text(row.get("company", ""))
    industry = clean_text(row.get("industry", ""))
    short_summary = clean_text(row.get("short_summary", ""))
    full_summary = clean_text(row.get("full_summary", ""))
    tools_tags = clean_text(row.get("tools_tags", ""))
    techniques_tags = clean_text(row.get("techniques_tags", ""))

    base_summary = short_summary or full_summary

    concise_summary = truncate_words(base_summary, max_words=45)

    context_bits = []

    if company:
        context_bits.append(company)

    if industry:
        context_bits.append(industry)

    context = " / ".join(context_bits)

    tags = []

    if tools_tags:
        tags.append(f"Tools: {tools_tags}")

    if techniques_tags:
        tags.append(f"Techniques: {techniques_tags}")

    tags_text = " | ".join(tags)

    parts = []

    if context:
        parts.append(f"**{context}**")

    if concise_summary:
        parts.append(concise_summary)
    elif title:
        parts.append(f"A noteworthy LLMOps item: {title}")

    if tags_text:
        parts.append(tags_text)

    return " — ".join(parts)


def load_records():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            "Database not found. Run `python ingest_dataset.py` first.")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM llmops_case_studies",
            conn,
        )

    return df


def process_and_analyze(top_n=25):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_records()

    week_start, week_end = get_current_week_window()

    print(f"Processing records: {len(df)}")
    print(f"Current week window: {week_start} to {week_end}")

    df["section"] = df.apply(categorize_item, axis=1)

    df["trending_score"] = df.apply(
        lambda row: compute_trending_score(row, week_start, week_end),
        axis=1,
    )

    df["newsletter_summary"] = df.apply(make_newsletter_summary, axis=1)

    df["week_start"] = str(week_start)
    df["week_end"] = str(week_end)

    # Sort by score, then recent year if available
    sort_cols = ["trending_score"]

    if "year" in df.columns:
        sort_cols.append("year")

    df = df.sort_values(
        by=sort_cols,
        ascending=False,
    )

    processed = df.head(top_n).copy()

    # Save to SQLite table
    with sqlite3.connect(DB_PATH) as conn:
        processed.to_sql(
            "processed_newsletter_items",
            conn,
            if_exists="replace",
            index=False,
        )

    # Save to JSONL
    with open(PROCESSED_JSONL_PATH, "w", encoding="utf-8") as f:
        for _, row in processed.iterrows():
            item = {
                "title": clean_text(row.get("title", "")),
                "company": clean_text(row.get("company", "")),
                "industry": clean_text(row.get("industry", "")),
                "year": clean_text(row.get("year", "")),
                "source_url": clean_text(row.get("source_url", "")),
                "section": clean_text(row.get("section", "")),
                "trending_score": int(row.get("trending_score", 0)),
                "newsletter_summary": clean_text(row.get("newsletter_summary", "")),
                "tools_tags": clean_text(row.get("tools_tags", "")),
                "techniques_tags": clean_text(row.get("techniques_tags", "")),
                "application_tags": clean_text(row.get("application_tags", "")),
            }

            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print("\nProcessing complete.")
    print(f"Processed table: processed_newsletter_items")
    print(f"Processed JSONL: {PROCESSED_JSONL_PATH}")

    print("\nTop items:")
    preview_cols = [
        "title",
        "company",
        "section",
        "trending_score",
    ]

    existing_preview_cols = [
        col for col in preview_cols if col in processed.columns]

    print(processed[existing_preview_cols].head(10).to_string(index=False))


if __name__ == "__main__":
    process_and_analyze(top_n=25)
