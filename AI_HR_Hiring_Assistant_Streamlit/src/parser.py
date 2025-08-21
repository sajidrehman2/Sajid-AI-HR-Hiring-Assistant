import re
from pdfminer.high_level import extract_text
import docx

def parse_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = " ".join([p.text for p in doc.paragraphs])
    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
    
    data = {
        "name": re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text[:100])[:1],
        "email": re.findall(r'[\w\.-]+@[\w\.-]+', text)[:1],
        "phone": re.findall(r'\+?\d[\d -]{8,12}\d', text)[:1],
    }
    return text, data
