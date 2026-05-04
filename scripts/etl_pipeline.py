"""
ETL Pipeline for Real Estate Analysis Project
"""

from pathlib import Path
import pandas as pd


# ─── Extract ───────────────────────────────────────────────
def extract(input_path: Path) -> pd.DataFrame:
    print("📥 Extracting data...")
    return pd.read_csv(input_path)


# ─── Transform (Cleaning + Feature Engineering) ────────────
def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("🧹 Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna(subset=["price_egp", "area_value"])

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("⚙️ Feature Engineering...")

    # Create KPI
    df["price_per_sqft"] = df["price_egp"] / df["area_value"]

    # Remove unrealistic values
    df = df[df["price_per_sqft"] > 0]

    return df


# ─── Load ─────────────────────────────────────────────────
def load(df: pd.DataFrame, output_path: Path):
    print("💾 Saving processed data...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# ─── Pipeline Runner ──────────────────────────────────────
def run_pipeline(input_path: str, output_path: str):
    df = extract(Path(input_path))
    df = transform(df)
    load(df, Path(output_path))

    print("✅ ETL Pipeline Completed Successfully!")


# ─── Main ─────────────────────────────────────────────────
if __name__ == "__main__":
    run_pipeline(
        "data/raw/propertyfinder.csv",
        "data/processed/cleaned_data.csv"
    )