import os
import json
import spacy
from tqdm import tqdm

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load fact-checked claims
input_path = os.path.join("data", "processed", "claims_fact_checked.json")
with open(input_path, "r", encoding="utf-8") as f:
    claims = json.load(f)

# Extract entities
results = []
print(f"🔍 Extracting named entities from {len(claims)} claims...")
for item in tqdm(claims):
    doc = nlp(item["claim"])
    entities = list(set(ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]))
    results.append({
        "claim": item["claim"],
        "source_title": item["source_title"],
        "fact_check_result": item["fact_check_result"],
        "entities": entities
    })

# Save output
output_path = os.path.join("data", "processed", "claims_with_entities.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"✅ Entities extracted and saved to {output_path}")
