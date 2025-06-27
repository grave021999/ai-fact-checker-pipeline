from sentence_transformers import SentenceTransformer, util
import wikipedia
import json
from pathlib import Path

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# File paths
input_path = Path("data/processed/claims_with_entities.jsonl")
output_path = Path("data/processed/claims_verified.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)

def search_wikipedia(query):
    try:
        results = wikipedia.search(query, results=1)
        if not results:
            return ""
        page = wikipedia.page(results[0])
        return page.content[:1000]  # Limit to 1000 chars
    except Exception as e:
        print(f"[!] Wikipedia error for '{query}': {e}")
        return ""

def verify_claims():
    with input_path.open("r", encoding="utf-8") as f_in, output_path.open("w", encoding="utf-8") as f_out:
        for line in f_in:
            record = json.loads(line)
            claim = record["original_title"]

            wiki_text = search_wikipedia(claim)
            if not wiki_text:
                record["verification"] = "Not Found"
                record["confidence"] = 0.0
            else:
                embeddings = model.encode([claim, wiki_text], convert_to_tensor=True)
                score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()

                record["verification"] = "Likely True" if score > 0.5 else "Uncertain"
                record["confidence"] = round(score, 3)

            f_out.write(json.dumps(record) + "\n")
            print(f"[✔] {claim} → {record['verification']} (Score: {record['confidence']})")

if __name__ == "__main__":
    verify_claims()
