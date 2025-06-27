import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# Load the final fact-checked claims
file_path = os.path.join("data", "processed", "claims_fact_checked.json")

# Step 1: Load JSON data
if not os.path.exists(file_path):
    print("❌ File not found:", file_path)
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Step 2: Plot fact-check result counts
plt.figure(figsize=(6, 4))
df["fact_check_result"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Fact Check Result Distribution")
plt.xlabel("Result")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Step 3: Plot most frequent named entities
all_entities = []
for item in df["entities"]:
    all_entities.extend(item)

top_entities = Counter(all_entities).most_common(10)

if top_entities:
    labels, values = zip(*top_entities)
    plt.figure(figsize=(6, 4))
    plt.barh(labels, values, color="lightgreen")
    plt.title("Top 10 Named Entities")
    plt.xlabel("Frequency")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ No entities found in data.")
