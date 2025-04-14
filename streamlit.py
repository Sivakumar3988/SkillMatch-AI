import streamlit as st
from resume import get_text
from match import rank_resumes

st.set_page_config(page_title = "SkillMatch AI", layout = "centered")
st.title("🤖 SkillMatch AI")
st.subheader("Smart Resume Matcher")

st.markdown("UPLOAD JOB DESCRIPTION")
job_text = ""
job_file = st.file_uploader("Upload job description(.txt, .pdf, .docx)", type = ["txt", "pdf", "docx"])
if job_file:
    job_text = get_text(job_file)

st.markdown("UPLOAD RESUMES")
resume_files = st.file_uploader("Upload multiple resumes", type = ["pdf", "docx"], accept_multiple_files = True)

if job_text and resume_files:
    st.markdown("Matching Results")
    resumes_data = []
    for file in resume_files:
        try:
            text = get_text(file)
            resumes_data.append({"name": file.name, "text": text})
        except Exception as e:
            st.error (f"Failed to read {file.name}: {e}")

    results = rank_resumes(resumes_data, job_text)

    for res in results:
        st.markdown(f"**📄 {res['name']}**")
        st.markdown(f"🔍 Match Score: `{res['score']}`")
        st.markdown(f"✅ Skills Matched: `{', '.join(res['skills']) if res['skills'] else 'No skills matched'}`")
        st.markdown("---")