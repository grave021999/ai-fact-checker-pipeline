import pandas as pd
import os
import json
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Path to validated data
input_path = os.path.join("data", "processed", "news_validated.json")
output_path = os.path.join("data", "processed", "claims_extracted.json")

# Load articles
df = pd.read_json(input_path, lines=True)


claims = []

for idx, row in df.iterrows():
    doc = nlp(row["title"])
    for sent in doc.sents:
        if len(sent.text.split()) > 5:  # Filter very short ones
            claims.append({
                "claim_id": f"news_{idx}_s{sent.start}",
                "text": sent.text.strip(),
                "source": row["link"],
                "title": row["title"]
            })

# Save extracted claims
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(claims, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(claims)} claims.")
print(f"📄 Saved to {output_path}")
