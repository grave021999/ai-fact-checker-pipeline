import os
import json
from tqdm import tqdm

# Load claims from JSON
input_path = os.path.join("data", "processed", "claims_extracted.json")
with open(input_path, "r", encoding="utf-8") as f:
    claims = json.load(f)

# Simple mock fact-checker
def mock_fact_check(claim_text):
    claim_lower = claim_text.lower()

    if "iran" in claim_lower or "nuclear" in claim_lower:
        return "False – Not supported by public data."
    elif "tehran" in claim_lower or "editor-in-chief" in claim_lower:
        return "True – Widely reported by credible sources."
    else:
        return "Uncertain – Not enough context to verify."

# Apply mock fact-checking
results = []
print(f"🧠 Fact-checking {len(claims)} claims (mock logic)...")
for claim in tqdm(claims):
    result = {
        "claim": claim.get("text"),
        "source_title": claim.get("title"),
        "fact_check_result": mock_fact_check(claim.get("text"))
    }
    results.append(result)

# Save results
output_path = os.path.join("data", "processed", "claims_fact_checked.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"✅ Mock fact-checking complete. Saved to {output_path}")
