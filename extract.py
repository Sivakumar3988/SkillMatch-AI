import re
import nltk
from nltk.corpus import stopwords
from skills_list import skills


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ',text)
    text = re.sub(r'[^\w\s]','',text)
    return text

def extract_skills(text: str) -> list:
    text = clean_text(text)
    found = set()
    for skill in skills:
        if skill.lower() in text:
            found.add(skill.lower())
    return list(found)

