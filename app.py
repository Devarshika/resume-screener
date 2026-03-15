import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screener", layout="wide")

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

st.title("AI Resume Screening System")
st.markdown("Upload resumes and compare them against a job description using semantic similarity.")

uploaded_files = st.file_uploader(
    "Upload candidate resumes (PDF only)", 
    type=["pdf"], 
    accept_multiple_files=True
)

job_description = st.text_area("Paste Job Description Here")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

if st.button("Rank Candidates"):
    if not uploaded_files or not job_description:
        st.warning("Please upload resumes and enter job description.")
    else:
        resume_texts = []
        names = []

        with st.spinner("Processing resumes..."):
            for file in uploaded_files:
                text = extract_text_from_pdf(file)
                resume_texts.append(text)
                names.append(file.name)

            jd_embedding = model.encode([job_description])
            resume_embeddings = model.encode(resume_texts)

            similarities = cosine_similarity(jd_embedding, resume_embeddings)[0]

            results = pd.DataFrame({
                "Candidate": names,
                "Match Score": similarities
            })

            results = results.sort_values(by="Match Score", ascending=False)

        st.success("Ranking Complete!")
        st.dataframe(results, use_container_width=True)