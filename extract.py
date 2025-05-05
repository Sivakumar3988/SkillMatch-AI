#Importing the required libraries
import re
import nltk
from nltk.corpus import stopwords
from skills_list import skills

# Download the list of stopwords from the NLTK library
nltk.download('stopwords')
# Importing the list of English stopwords into a Python
stop_words = set(stopwords.words('english'))

# Function to clean input text by lowercasing, removing extra spaces, and punctuation
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ',text)
    text = re.sub(r'[^\w\s]','',text)
    return text

# Function to extract matching skills from the cleaned text
def extract_skills(text: str) -> list:
    text = clean_text(text)
    found = set()
    for skill in skills:
        if skill.lower() in text:
            found.add(skill.lower())
    return list(found)

