from datasets import load_dataset
import pandas as pd
import sqlite3
from pathlib import Path


DATASET_NAME = "zenml/llmops-database"
OUTPUT_DIR = Path("data/llmops_database")
SQLITE_DB_PATH = OUTPUT_DIR / "llmops_database.db"


def normalize_tag_field(value):
    """
    Hugging Face datasets can store tag-like fields as lists or strings.
    This function converts them into a clean comma-separated string.
    """
    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(str(v).strip() for v in value if v)

    return str(value).strip()


def ingest_dataset():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading dataset: {DATASET_NAME}")

    dataset = load_dataset(DATASET_NAME)

    print("Available splits:", dataset.keys())

    # The dataset page says it has a single collection.
    # Usually Hugging Face exposes this as "train".
    split_name = list(dataset.keys())[0]
    records = dataset[split_name]

    df = records.to_pandas()

    print(f"Loaded {len(df)} records")
    print("Columns:", list(df.columns))

    # Expected fields from the dataset card
    expected_columns = [
        "created_at",
        "title",
        "industry",
        "year",
        "source_url",
        "company",
        "application_tags",
        "tools_tags",
        "extra_tags",
        "techniques_tags",
        "short_summary",
        "full_summary",
    ]

    # Keep only columns that exist, in case the dataset schema changes later
    available_columns = [col for col in expected_columns if col in df.columns]
    df = df[available_columns].copy()

    # Normalize dates
    if "created_at" in df.columns:
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    # Normalize year
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    # Normalize tag fields
    tag_columns = [
        "application_tags",
        "tools_tags",
        "extra_tags",
        "techniques_tags",
    ]

    for col in tag_columns:
        if col in df.columns:
            df[col] = df[col].apply(normalize_tag_field)

    # Remove records without title
    if "title" in df.columns:
        df = df[df["title"].notna()]
        df["title"] = df["title"].astype(str).str.strip()

    # Add a derived text field useful for newsletter/RAG workflows
    text_parts = []

    for col in [
        "title",
        "company",
        "industry",
        "short_summary",
        "full_summary",
        "application_tags",
        "tools_tags",
        "techniques_tags",
    ]:
        if col in df.columns:
            text_parts.append(df[col].fillna("").astype(str))

    if text_parts:
        df["newsletter_context"] = text_parts[0]
        for part in text_parts[1:]:
            df["newsletter_context"] += "\n" + part

        df["newsletter_context"] = df["newsletter_context"].str.strip()

    # Save as CSV
    csv_path = OUTPUT_DIR / "llmops_database.csv"
    df.to_csv(csv_path, index=False)

    # Save as JSONL
    jsonl_path = OUTPUT_DIR / "llmops_database.jsonl"
    df.to_json(jsonl_path, orient="records", lines=True, force_ascii=False)

    # Save as Parquet
    parquet_path = OUTPUT_DIR / "llmops_database.parquet"
    df.to_parquet(parquet_path, index=False)

    # Save to SQLite
    with sqlite3.connect(SQLITE_DB_PATH) as conn:
        df.to_sql("llmops_case_studies", conn,
                  if_exists="replace", index=False)

    print("\nIngestion complete.")
    print(f"CSV saved to:     {csv_path}")
    print(f"JSONL saved to:   {jsonl_path}")
    print(f"Parquet saved to: {parquet_path}")
    print(f"SQLite saved to:  {SQLITE_DB_PATH}")

    return df


if __name__ == "__main__":
    df = ingest_dataset()

    print("\nSample records:")
    print(df[["title", "company", "industry"]].head(5))
