import spacy
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Predefined skill list (can be extended)
SKILL_SET = ["Python", "Flask", "Django", "Machine Learning", "Deep Learning", "SQL", "NLP", "Pandas", "Data Science", "TensorFlow"]

def analyze_resume(text):
    doc = nlp(text)
    extracted_skills = [skill for skill in SKILL_SET if skill.lower() in text.lower()]
    
    # Summarize (simple for now)
    summary = f"Your resume highlights skills in {', '.join(extracted_skills)}. You could strengthen it by adding measurable achievements and project outcomes."
    return extracted_skills, summary
