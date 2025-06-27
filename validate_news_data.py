import os
import pandas as pd

# ✅ Step 1: Load the data
df_path = os.path.join("data", "raw", "news_rss.jsonl")
print("✅ File exists:", os.path.exists(df_path))
df = pd.read_json(df_path, lines=True)

# ✅ Step 2: Custom validation checks
errors = []

# Check for required columns
required_columns = ["title", "link"]  # remove 'pubDate'

for col in required_columns:
    if col not in df.columns:
        errors.append(f"❌ Missing column: {col}")
    elif df[col].isnull().any():
        errors.append(f"❌ Null values found in column: {col}")

# ✅ Step 3: Show results
if errors:
    print("❌ Data validation failed with following issues:")
    for e in errors:
        print("-", e)
    exit(1)
else:
    print("✅ Data validation passed successfully.")

# ✅ Step 4: Save clean version (optional)
df.to_json("data/processed/news_validated.json", orient="records", lines=True)
print("📦 Cleaned data saved to processed/news_validated.json")
