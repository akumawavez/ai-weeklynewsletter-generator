import sqlite3
from pathlib import Path
from datetime import date
from collections import defaultdict


DB_PATH = Path("data/llmops_database.db")
OUTPUT_DIR = Path("newsletter_outputs")


SECTION_ORDER = [
    "Research Highlights",
    "Industry News",
    "Cool Use Cases",
    "Tools & Infrastructure",
    "Other Noteworthy Items",
]


def fetch_processed_items():
    query = """
    SELECT
        title,
        company,
        industry,
        year,
        source_url,
        section,
        trending_score,
        newsletter_summary,
        tools_tags,
        techniques_tags,
        application_tags
    FROM processed_newsletter_items
    ORDER BY trending_score DESC
    """

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(query).fetchall()

    return rows


def generate_markdown_newsletter():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            "Database not found. Run `python ingest_dataset.py` first.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rows = fetch_processed_items()

    grouped = defaultdict(list)

    for row in rows:
        (
            title,
            company,
            industry,
            year,
            source_url,
            section,
            trending_score,
            newsletter_summary,
            tools_tags,
            techniques_tags,
            application_tags,
        ) = row

        grouped[section].append(
            {
                "title": title,
                "company": company,
                "industry": industry,
                "year": year,
                "source_url": source_url,
                "section": section,
                "trending_score": trending_score,
                "newsletter_summary": newsletter_summary,
                "tools_tags": tools_tags,
                "techniques_tags": techniques_tags,
                "application_tags": application_tags,
            }
        )

    today = date.today().isoformat()

    lines = [
        f"# Weekly LLMOps Newsletter — {today}",
        "",
        "A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.",
        "",
        "## This Week’s Angle",
        "",
        "This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.",
        "",
    ]

    for section in SECTION_ORDER:
        items = grouped.get(section, [])

        if not items:
            continue

        lines.extend(
            [
                f"## {section}",
                "",
            ]
        )

        for idx, item in enumerate(items, start=1):
            title = item["title"] or "Untitled"
            company = item["company"] or "Unknown company"
            industry = item["industry"] or "Unknown industry"
            source_url = item["source_url"] or ""
            summary = item["newsletter_summary"] or "No summary available."
            score = item["trending_score"]

            lines.extend(
                [
                    f"### {idx}. {title}",
                    "",
                    f"**Company:** {company}",
                    "",
                    f"**Industry:** {industry}",
                    "",
                    f"**Relevance score:** {score}",
                    "",
                    summary,
                    "",
                ]
            )

            if source_url:
                lines.extend(
                    [
                        f"**Source:** {source_url}",
                        "",
                    ]
                )

            lines.append("---")
            lines.append("")

    output_path = OUTPUT_DIR / f"llmops_newsletter_{today}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Newsletter generated: {output_path}")


if __name__ == "__main__":
    generate_markdown_newsletter()
