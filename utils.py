import PyPDF2
import docx
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)

    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = " ".join(
        word for word in text.split()
        if word not in stopwords.words('english')
    )
    return text

vectorizer = TfidfVectorizer()

def match_resume_job(resume_text, job_text):
    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)
SKILLS = [
    "python", "machine learning", "data science", "nlp",
    "pandas", "numpy", "sql", "streamlit"
]

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text.lower():
            found.append(skill)
    return found
