import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path


DB_PATH = Path("data/llmops_database.db")


@st.cache_data
def load_data():
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM llmops_case_studies",
            conn,
        )
    return df


st.set_page_config(
    page_title="LLMOps Case Study Explorer",
    layout="wide",
)

st.title("LLMOps Case Study Explorer")

if not DB_PATH.exists():
    st.error("Database not found. Run `python ingest_dataset.py` first.")
    st.stop()

df = load_data()

st.sidebar.header("Filters")

search_text = st.sidebar.text_input("Search title, company, summary, tags")

industries = sorted(df["industry"].dropna().unique()
                    ) if "industry" in df.columns else []
selected_industries = st.sidebar.multiselect("Industry", industries)

companies = sorted(df["company"].dropna().unique()
                   ) if "company" in df.columns else []
selected_companies = st.sidebar.multiselect("Company", companies)

filtered = df.copy()

if search_text:
    search_text_lower = search_text.lower()

    searchable_cols = [
        "title",
        "company",
        "industry",
        "short_summary",
        "full_summary",
        "tools_tags",
        "techniques_tags",
        "application_tags",
    ]

    existing_cols = [col for col in searchable_cols if col in filtered.columns]

    mask = False
    for col in existing_cols:
        mask = mask | filtered[col].fillna("").astype(
            str).str.lower().str.contains(search_text_lower)

    filtered = filtered[mask]

if selected_industries:
    filtered = filtered[filtered["industry"].isin(selected_industries)]

if selected_companies:
    filtered = filtered[filtered["company"].isin(selected_companies)]

st.subheader(f"Results: {len(filtered)} case studies")

for _, row in filtered.iterrows():
    with st.expander(f"{row.get('title', 'Untitled')} — {row.get('company', '')}"):
        st.write(f"**Industry:** {row.get('industry', '')}")
        st.write(f"**Year:** {row.get('year', '')}")
        st.write(f"**Company:** {row.get('company', '')}")

        if row.get("source_url"):
            st.write(f"**Source:** {row.get('source_url')}")

        st.write("### Summary")
        st.write(row.get("short_summary", ""))

        st.write("### Tags")
        st.write(f"**Tools:** {row.get('tools_tags', '')}")
        st.write(f"**Techniques:** {row.get('techniques_tags', '')}")
        st.write(f"**Applications:** {row.get('application_tags', '')}")

        with st.expander("Full summary"):
            st.write(row.get("full_summary", ""))
