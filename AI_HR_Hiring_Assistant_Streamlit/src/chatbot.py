import pandas as pd
from sentence_transformers import SentenceTransformer, util

faq = pd.read_csv("data/faq.csv")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
faq_embeddings = model.encode(faq["question"].tolist(), convert_to_tensor=True)

def get_answer(query):
    q_emb = model.encode(query, convert_to_tensor=True)
    sims = util.cos_sim(q_emb, faq_embeddings)
    best = sims.argmax().item()
    return faq.iloc[best]["answer"]
