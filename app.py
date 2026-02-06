import streamlit as st
from utils import extract_text, clean_text, match_resume_job, extract_skills, SKILLS

st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("Resume Screening & Job Matching System")

resume = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description Here")

if resume and job_desc:
    resume_text = clean_text(extract_text(resume))
    job_text = clean_text(job_desc)

    score = match_resume_job(resume_text, job_text)
    st.success(f"Match Score: {score}%")

    # ----- Skill Analysis -----
    skills_found = extract_skills(resume_text)
    missing_skills = list(set(SKILLS) - set(skills_found))

    st.subheader("Skills Analysis")

    st.write("Skills Found:")
    st.write(skills_found if skills_found else "None")

    st.write("Missing Skills:")
    st.write(missing_skills if missing_skills else "None")

