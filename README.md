# SkillMatch-AI

SkillMatch AI is an intelligent resume screening tool that helps match candidates to job descriptions using NLP and semantic similarity. It's designed for hiring teams, recruiters, and career platforms to go beyond keyword filters and uncover the best talent based on real skills.

# How SkillMatch AI Is Different from Traditional Keyword-Based ATS Software

Most Applicant Tracking Systems (ATS) use exact keyword matching. If a job post mentions “data visualization” and your resume says “built charts with Matplotlib,” you might get overlooked — even if you’re a perfect fit.

**SkillMatch AI**, on the other hand, uses semantic understanding powered by NLP models. It doesn't just look for what words are used — **it understands what they mean.**

## 🔍 Features

- Upload job descriptions (.txt, .pdf, .docx)
- Upload multiple resumes (.pdf, .docx)
- Automatically extracts and matches skills
- Ranks candidates by semantic similarity using `sentence-transformers`
- Clean Streamlit interface for use or demo

## 📦 Tech Stack

- Python
- Streamlit
- sentence-transformers (`all-MiniLM-L6-v2`)
- Scikit-learn
- NLTK
- pdfplumber / python-docx
