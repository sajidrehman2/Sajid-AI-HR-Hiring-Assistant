# AI HR & Hiring Assistant (Streamlit • Free/Open-Source)

An end-to-end **AI HR Assistant** you can deploy **for free** on Streamlit Cloud:

- 📄 **Resume Parser**: PDF/DOCX/TXT to structured fields (name, email, phone, skills, years).
- 🧠 **Candidate Ranking**: Combines **semantic similarity** (Sentence-Transformers) + **skills match**.
- 📊 **Hire Prediction (toy)**: Trains a lightweight classifier on synthetic past data.
- 🤖 **Chatbot (no paid keys)**: FAQ retrieval bot over `data/faq.csv` using embeddings.
- 🌐 **Streamlit app**: Upload multiple resumes, paste/upload a Job Description, rank, export CSV.
- 🆓 100% **free** libraries + models (no API keys).

---

## 1) Local Run

```bash
# 1) Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the app
streamlit run app.py
```

The first run will **download a small Sentence-Transformers model**. Keep the terminal open.

---

## 2) Deploy on Streamlit Cloud (Free)

1. Create a new **GitHub** repo and upload all project files (or drag-drop the provided ZIP).
2. Go to **share.streamlit.io** → **New app**.
3. Select your repo, main branch, and set **Main file path** to `app.py`.
4. (Optional) In **Advanced settings**, set **Python version** to `3.10` or `3.11`.
5. Click **Deploy**. First boot will install deps & download model.
6. Use the app URL to share your live demo.

> **Tip:** If build times out, try re-running or switching region. Streamlit Cloud free tier is CPU-only, which is fine for this app.

---

## 3) Project Structure

```
AI_HR_Hiring_Assistant_Streamlit/
├── app.py
├── requirements.txt
├── LICENSE
├── README.md
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── ranking.py
│   ├── chatbot.py
│   └── model.py
└── data/
    ├── skills_taxonomy.csv
    ├── faq.csv
    ├── hiring_history.csv
    ├── job_descriptions/
    │   └── sample_jd.txt
    └── resumes/
        ├── sample_resume_1.txt
        ├── sample_resume_2.txt
        └── sample_resume_3.docx
```

---

## 4) Notes

- **No paid APIs** are used. All models are open-source (Hugging Face sentence-transformers, scikit-learn).
- PDF parsing uses `pdfminer.six`; DOCX uses `python-docx`.
- The **hire prediction** is trained on a **synthetic** dataset only for demo purposes.
- For best results, provide a clear Job Description and realistic resumes.
- You can extend skills by editing `data/skills_taxonomy.csv` and FAQ content in `data/faq.csv`.

Enjoy! 🚀
