import streamlit as st
import pandas as pd

# Sample job data
JOBS = [
    {"title": "Machine Learning Engineer", "company": "Google", "location": "Bangalore, India",
     "type": "Full-time", "skills": "Python, TensorFlow, MLOps", "salary": "₹25-40 LPA", "category": "ML/AI"},
    {"title": "Data Scientist", "company": "Microsoft", "location": "Hyderabad, India",
     "type": "Full-time", "skills": "Python, SQL, Power BI, Azure", "salary": "₹20-35 LPA", "category": "Data Science"},
    {"title": "AI Research Engineer", "company": "Amazon", "location": "Remote",
     "type": "Full-time", "skills": "Deep Learning, NLP, PyTorch", "salary": "₹30-50 LPA", "category": "ML/AI"},
    {"title": "Cloud Data Engineer", "company": "TATA Consultancy Services", "location": "Chennai, India",
     "type": "Full-time", "skills": "GCP, BigQuery, Airflow, Terraform", "salary": "₹18-30 LPA", "category": "Cloud"},
    {"title": "MLOps Engineer", "company": "Infosys", "location": "Pune, India",
     "type": "Full-time", "skills": "Kubernetes, Docker, CI/CD, Tekton", "salary": "₹15-25 LPA", "category": "MLOps"},
    {"title": "NLP Engineer", "company": "Flipkart", "location": "Bangalore, India",
     "type": "Full-time", "skills": "BERT, Transformers, spaCy, Python", "salary": "₹20-32 LPA", "category": "ML/AI"},
    {"title": "Data Analyst", "company": "TCS", "location": "Mumbai, India",
     "type": "Full-time", "skills": "SQL, Excel, Tableau, Python", "salary": "₹8-15 LPA", "category": "Data Science"},
    {"title": "Computer Vision Engineer", "company": "Ola", "location": "Bangalore, India",
     "type": "Full-time", "skills": "OpenCV, CNN, YOLO, PyTorch", "salary": "₹18-28 LPA", "category": "ML/AI"},
    {"title": "GCP Data Engineer", "company": "Wipro", "location": "Hyderabad, India",
     "type": "Contract", "skills": "BigQuery, Dataflow, Pub/Sub, Python", "salary": "₹12-22 LPA", "category": "Cloud"},
    {"title": "AI Product Manager", "company": "Razorpay", "location": "Bangalore, India",
     "type": "Full-time", "skills": "AI/ML concepts, Product Strategy, SQL", "salary": "₹25-45 LPA", "category": "Product"},
]

def show():
    st.markdown("## 💼 AI & Tech Job Search")
    st.markdown("Find your next role in AI, ML, Data Science & Cloud")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        search = st.text_input("🔍 Search by title or skill", placeholder="e.g. Machine Learning")
    with col2:
        category = st.selectbox("📂 Category", ["All", "ML/AI", "Data Science", "Cloud", "MLOps", "Product"])
    with col3:
        job_type = st.selectbox("⏱ Job Type", ["All", "Full-time", "Contract", "Remote"])

    st.markdown("---")

    # Filter jobs
    filtered = JOBS
    if search:
        filtered = [j for j in filtered if search.lower() in j["title"].lower()
                    or search.lower() in j["skills"].lower()]
    if category != "All":
        filtered = [j for j in filtered if j["category"] == category]
    if job_type == "Remote":
        filtered = [j for j in filtered if "Remote" in j["location"]]
    elif job_type != "All":
        filtered = [j for j in filtered if j["type"] == job_type]

    st.markdown(f"**{len(filtered)} jobs found**")

    for job in filtered:
        with st.container():
            st.markdown(f"""
            <div style='background:white; padding:1.2rem 1.5rem; border-radius:12px;
                        border-left: 5px solid #1a73e8; margin-bottom:1rem;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.07);'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <h4 style='margin:0; color:#0d1b2a;'>{job["title"]}</h4>
                        <p style='margin:4px 0; color:#1a73e8; font-weight:600;'>{job["company"]}</p>
                        <p style='margin:2px 0; color:#555; font-size:0.9rem;'>
                            📍 {job["location"]} &nbsp;|&nbsp; ⏱ {job["type"]} &nbsp;|&nbsp; 💰 {job["salary"]}
                        </p>
                        <p style='margin:4px 0; color:#777; font-size:0.85rem;'>🛠 {job["skills"]}</p>
                    </div>
                    <span style='background:#e8f0fe; color:#1a73e8; padding:4px 12px;
                                 border-radius:20px; font-size:0.8rem; font-weight:600;'>
                        {job["category"]}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("💡 Tip: Use the AI Chatbot to get interview tips and resume advice for any of these roles!")
