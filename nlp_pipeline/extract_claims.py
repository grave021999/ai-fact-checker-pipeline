import spacy
import json
from pathlib import Path

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Input: from Step 1
input_file = Path("data/raw/news_rss.jsonl")

# Output: to Step 2
output_file = Path("data/processed/claims_with_entities.jsonl")
output_file.parent.mkdir(parents=True, exist_ok=True)

def extract_claims():
    with input_file.open("r", encoding="utf-8") as f_in, output_file.open("w", encoding="utf-8") as f_out:
        for line in f_in:
            data = json.loads(line)
            title = data.get("title", "")
            doc = nlp(title)

            # Extract named entities
            entities = list(set(ent.text for ent in doc.ents if ent.label_ in {
                "PERSON", "ORG", "GPE", "PRODUCT", "EVENT"
            }))

            output = {
                "original_title": title,
                "entities": entities,
                "published": data.get("published", ""),
                "source": data.get("source", ""),
                "link": data.get("link", "")
            }

            f_out.write(json.dumps(output) + "\n")
            print(f"[✔] Extracted: {title}")

if __name__ == "__main__":
    extract_claims()
