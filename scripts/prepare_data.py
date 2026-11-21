"""Prepare the Heart Failure dataset for analysis.

Reads the raw CSV (never modified) and writes a processed copy:
  - renames DEATH_EVENT to death_event
  - checks missing values and duplicates (drops duplicates if any)
  - adds an age_group column
Run from the project root:  python scripts/prepare_data.py
"""
import pandas as pd

RAW = "data/raw/heart_failure_clinical_records_dataset.csv"
OUT = "data/processed/heart_failure_clean.csv"

df = pd.read_csv(RAW)
df = df.rename(columns={"DEATH_EVENT": "death_event"})

print("Missing values :", df.isnull().sum().sum())
print("Duplicate rows :", df.duplicated().sum())
df = df.drop_duplicates()

bins = [39, 49, 59, 69, 79, 100]
labels = ["40-49", "50-59", "60-69", "70-79", "80+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

df.to_csv(OUT, index=False)
print("Saved", OUT, "with shape", df.shape)
