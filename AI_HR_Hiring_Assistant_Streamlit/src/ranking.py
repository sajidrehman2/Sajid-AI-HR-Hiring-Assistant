from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text):
    return model.encode(text, convert_to_tensor=True)

def rank_resume(resume_text, jd_vec):
    res_vec = embed_text(resume_text)
    score = float(util.cos_sim(res_vec, jd_vec)[0][0])
    return score
