# AI Resume Screening System

An AI-assisted resume ranking system that compares candidate resumes against a job description using semantic similarity.
The system helps recruiters prioritize high-relevance candidates while maintaining human-in-the-loop decision making.
## Problem
Recruiters often receive thousands of resumes for a single role.  
Manual screening is slow, inconsistent, and prone to bias.
This project demonstrates how AI can assist recruiters by ranking resumes based on relevance to a job description.
## Solution
The system uses NLP embeddings to represent resumes and job descriptions as vectors.
Cosine similarity is then used to measure how closely each resume matches the job requirements.
Candidates are ranked from highest to lowest relevance.

## Features
- Upload multiple resumes (PDF)
- Enter a job description
- AI-based semantic ranking
- Candidate match scores
- Interactive web interface

## Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyPDF2
- Pandas

## How It Works
1. Resumes are uploaded through the Streamlit interface.
2. Text is extracted from the PDF files.
3. Sentence-transformer embeddings convert text into numerical vectors.
4. Cosine similarity compares resume vectors with the job description vector.
5. Candidates are ranked based on similarity score.
## Example Output

| Candidate | Match Score |
|-----------|-------------|
| candidate1.pdf | 0.82 |
| candidate2.pdf | 0.74 |
| candidate3.pdf | 0.61 |

Higher score indicates stronger semantic match with the job description.
## Running the Project
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py
