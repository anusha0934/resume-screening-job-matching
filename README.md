# Resume Screening & Job Matching System

**Live Application: https://qpgrevkp4vssa6gkyrf2mx.streamlit.app/  
**GitHub Repository:** https://github.com/anusha0934/resume-screening-job-matching

---

## 📌 Project Overview

The **Resume Screening & Job Matching System** is an AI-powered web application designed to evaluate how well a candidate’s resume matches a given job description.  
It uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to calculate a match score and analyze technical skill alignment.

This project simulates a simplified **Applicant Tracking System (ATS)** used by recruiters and hiring platforms.

---

## 🚀 Features

- Upload resume in **PDF or DOCX** format
- Paste job description text
- Resume–Job **match score** using NLP
- **Skill extraction** from resume
- Identification of **missing skills**
- Interactive and user-friendly **Streamlit UI**
- Deployed live using **Streamlit Community Cloud**

---

## 🧠 How It Works

1. Resume and job description text are extracted and cleaned
2. Text is converted into numerical vectors using **TF-IDF**
3. **Cosine similarity** is used to compute the match score
4. Predefined technical skills are extracted from resume text
5. Skills found and missing skills are displayed clearly

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **Machine Learning:** Scikit-learn  
- **NLP Techniques:** TF-IDF, Cosine Similarity  
- **Libraries:** Pandas, NumPy, PyPDF2, python-docx  

---

## 📂 Project Structure

resume_job_matcher/
│
├── app.py # Main Streamlit application
├── utils.py # Text processing & NLP utilities
├── requirements.txt # Project dependencies
├── README.md # Project documentation

---

## ▶️ How to Run Locally

step 1: Clone the repository
git clone https://github.com/anusha0934/resume-screening-job-matching.git
cd resume-screening-job-matching
step 2: Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
step 3: Install dependencies
pip install -r requirements.txt
step 4: Run the application
streamlit run app.py

---

## Use Case

-Resume screening for recruiters
-Job-fit analysis for candidates
-ATS-style project for ML/NLP portfolios
-Academic and placement projects

---

## Future Enhancements

-Advanced skill extraction using spaCy
-Section-wise scoring (skills, experience, education)
-Resume ranking for multiple candidates
-Downloadable match report (PDF)
-Database integration for storage

---

## Author
Anusha K A
Mysore, Karnataka



