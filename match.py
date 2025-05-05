#Importing the required libraries
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from extract import clean_text, extract_skills

# Load the pre-trained sentence transformer model for embedding text
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to generate an embedding vector from cleaned input text
def embed_text(text: str):
    return model.encode([clean_text(text)]) [0]

# Function to rank resumes based on their similarity to the job description
def rank_resumes(resumes, job_description: str):
    job_vec = embed_text(job_description)
    ranked = []

    for resume in resumes:
        resume_vec = embed_text(resume['text'])
        score = cosine_similarity([job_vec],[resume_vec]) [0][0]
        ranked.append({
            "name" : resume['name'],
            "score" : round(float(score), 4),
            "skills" : extract_skills(resume['text']),   
        })
        
# Return the list of resumes sorted by similarity score in descending order
    return sorted(ranked, key = lambda x: x["score"], reverse = True)

