# retrieval.py
import json
from collections import defaultdict

DATA_PATH = "data/cleaned/recipes_2k_clean.jsonl"

print("🔄 Loading recipe data...")
recipes = [json.loads(line) for line in open(DATA_PATH, encoding="utf-8")]

# Build ingredient → recipes index
index = defaultdict(list)
for r in recipes:
    for ing in r["ingredients"].lower().split(","):
        ing = ing.strip()
        if len(ing) > 1:
            index[ing].append(r)

print(f"✅ Indexed {len(index)} unique ingredients from {len(recipes)} recipes.")

def find_best_match(user_input: str):
    tokens = [t.strip().lower() for t in user_input.split(",")]
    scores = defaultdict(int)

    for token in tokens:
        for recipe in index.get(token, []):
            scores[recipe["title"]] += 1

    if not scores:
        return None

    best_title = max(scores, key=scores.get)
    for r in recipes:
        if r["title"] == best_title:
            return r
    return None

# Test retrieval
if __name__ == "__main__":
    result = find_best_match("chicken, onion")
    if result:
        print(f"🍳 Found Recipe: {result['title']}")
        print(f"Ingredients: {result['ingredients']}")
        print(f"Instructions: {result['instructions']}")
    else:
        print("❌ No match found.")
