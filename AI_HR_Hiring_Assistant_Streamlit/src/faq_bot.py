import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Build absolute path to faq.csv
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # goes up from /src/
faq_path = os.path.join(BASE_DIR, "data", "faq.csv")

# Load FAQ data
faq = pd.read_csv(faq_path)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Encode FAQ questions
faq_embeddings = model.encode(faq["question"].tolist(), convert_to_tensor=True)

def get_answer(query: str) -> str:
    """Return the most relevant answer for a given query"""
    q_emb = model.encode(query, convert_to_tensor=True)
    sims = util.cos_sim(q_emb, faq_embeddings)
    best_idx = sims.argmax().item()
    return faq.iloc[best_idx]["answer"]

# Example test
if __name__ == "__main__":
    test_query = "What skills do I need?"
    print("Q:", test_query)
    print("A:", get_answer(test_query))
