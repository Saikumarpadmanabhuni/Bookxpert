from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import re
import unicodedata
from unidecode import unidecode

def load_names(file_path="names.txt"):
    """Load names from a text file (one name per line)."""
    with open(file_path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    return names


def normalize_name(s: str) -> str:
    s = s.strip()
    s = unicodedata.normalize("NFKD", s)
    s = unidecode(s)
    s = s.lower()
    s = re.sub(r'[^a-z\s]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s

def build_embeddings(names):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    names_norm = [normalize_name(n) for n in names]
    embeddings = model.encode(names_norm, convert_to_numpy=True, normalize_embeddings=True)
    return model, names_norm, embeddings

def build_faiss_index(embeddings):
    d = embeddings.shape[1] 
    index = faiss.IndexFlatIP(d)
    index.add(embeddings)
    return index

def search_similar_names(query_name, model, index, names, top_k=10):
    """Search top-k similar names using FAISS."""
    query_norm = normalize_name(query_name)
    query_emb = model.encode([query_norm], convert_to_numpy=True, normalize_embeddings=True)

    scores, indices = index.search(query_emb, top_k)
    scores = scores[0]  
    indices = indices[0]

    results = []
    for i, score in zip(indices, scores):
        results.append((names[i], float(score)))

    return results

def main():
    try:
        names = load_names("names.txt")
    except FileNotFoundError:
        print("File not found.")
        return
    model, names_norm, embeddings = build_embeddings(names)
    index = build_faiss_index(embeddings)
    while True:
        print("\n---------------------------------------------")
        query = input(" Enter a name to search (or type 'exit' to quit): ").strip()
        if not query:
            print(" Please enter a valid name.")
            continue
        if query.lower() in ["exit", "quit"]:
            print("Exit!!")
            break

        results = search_similar_names(query, model, index, names, top_k=10)

        print("\n Best Match:")
        print(f"   {results[0][0]}  (Similarity: {results[0][1]:.3f})")

        print("\n Similar Matches:")
        for rank, (name, score) in enumerate(results, start=1):
            print(f"{rank}. {name:<25}  Score: {score:.3f}")


if __name__ == "__main__":
    main()
