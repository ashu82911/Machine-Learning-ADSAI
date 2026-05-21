import streamlit as st
from pages import home, jobs, chatbot, knowledge, ford_overview

st.set_page_config(
    page_title="AshTech AI Portal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0d1b2a 0%, #1b2a4a 100%); }
    [data-testid="stSidebar"] * { color: #e0e0e0 !important; }
    .main { background-color: #f4f6fb; }
    .stButton>button {
        background: linear-gradient(90deg, #1a73e8, #0d47a1);
        color: white; border-radius: 8px; border: none;
        padding: 0.5rem 1.5rem; font-weight: 600;
    }
    .stButton>button:hover { background: linear-gradient(90deg, #0d47a1, #1a73e8); }
    h1, h2, h3 { color: #0d1b2a; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.markdown("## 🤖 AshTech AI Portal")
    st.markdown("---")
    page = st.radio("Navigate", [
        "🏠 Home",
        "💼 Job Search",
        "🤖 AI Chatbot",
        "📚 Knowledge Base",
        "📊 Ford Overview"
    ])
    st.markdown("---")
    st.markdown("**Built by** Ashutosh Kumar Pandey")
    st.markdown("📧 ashu82911@github.com")

# Route pages
if page == "🏠 Home":
    home.show()
elif page == "💼 Job Search":
    jobs.show()
elif page == "🤖 AI Chatbot":
    chatbot.show()
elif page == "📚 Knowledge Base":
    knowledge.show()
elif page == "📊 Ford Overview":
    ford_overview.show()
