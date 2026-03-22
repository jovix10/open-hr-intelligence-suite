import streamlit as st
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text.lower()
    except Exception as e:
        st.error(f"Erro ao ler {pdf_file.name}")
        return ""

def run_recruiter():
    st.markdown("### 🔍 Recrutador IA")
    st.caption("Analise a compatibilidade de currículos com a vaga desejada.")
    
    col1, col2 = st.columns(2)
    with col1:
        job_desc = st.text_area("Requisitos da Vaga", placeholder="Ex: Python, Flask, SQL...", height=150)
    with col2:
        files = st.file_uploader("Currículos (PDF)", accept_multiple_files=True, type="pdf")

    if st.button("Analisar") and job_desc and files:
        keywords = [w.lower() for w in job_desc.split() if len(w) > 3]
        results = []
        
        for f in files:
            txt = extract_text_from_pdf(f)
            score = sum(1 for w in keywords if w in txt)
            match = (score / len(keywords)) * 100 if keywords else 0
            results.append({"Candidato": f.name, "Match": f"{match:.1f}%"})
        
        st.divider()
        st.table(sorted(results, key=lambda x: x['Match'], reverse=True))