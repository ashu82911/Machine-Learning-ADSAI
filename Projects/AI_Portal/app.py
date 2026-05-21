import streamlit as st
from pages import home, jobs, chatbot, knowledge, tata_overview, feed, profile, network

st.set_page_config(
    page_title="FacebookIndia AI",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f1e 0%, #0d1b2a 50%, #1a237e 100%) !important;
    border-right: 1px solid #1a73e8;
}
[data-testid="stSidebar"] * { color: #e8eaf6 !important; }
[data-testid="stSidebar"] .stRadio label { 
    padding: 8px 12px; border-radius: 8px; transition: all 0.2s;
}
.main { background: #f0f2f5; }
.stButton>button {
    background: linear-gradient(90deg, #1a73e8, #1565c0);
    color: white !important; border-radius: 10px; border: none;
    padding: 0.5rem 1.5rem; font-weight: 600; transition: all 0.3s;
    box-shadow: 0 2px 8px rgba(26,115,232,0.3);
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1565c0, #0d47a1);
    box-shadow: 0 4px 16px rgba(26,115,232,0.5); transform: translateY(-1px);
}
.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    border-radius: 10px; border: 1.5px solid #e0e0e0;
    background: white; padding: 0.6rem 1rem;
}
.stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
    border-color: #1a73e8; box-shadow: 0 0 0 3px rgba(26,115,232,0.15);
}
div[data-testid="stChatMessage"] { background: white; border-radius: 14px; margin: 6px 0; }
.stTabs [data-baseweb="tab"] { border-radius: 8px 8px 0 0; font-weight: 600; }
.stTabs [aria-selected="true"] { background: #1a73e8; color: white !important; }
hr { border: none; border-top: 1px solid #e8eaf6; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

# Session state defaults
if "username" not in st.session_state:
    st.session_state.username = "Ashu"
if "posts" not in st.session_state:
    st.session_state.posts = [
        {"id": 1, "user": "Ashu", "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu",
         "text": "🚀 Just launched FacebookIndia AI Portal! Built with Python + Streamlit. AI-powered job search, chatbot & social feed all in one place. #AI #Python #Innovation",
         "image": "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=600&q=80",
         "likes": 42, "liked_by": [], "comments": ["Amazing work Ashu! 🔥", "This is incredible!", "Congrats 🎉"], "time": "2h ago"},
        {"id": 2, "user": "Priya Sharma", "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Priya",
         "text": "🎯 Excited to share that I cleared my Google ML Engineer interview! Key topics: System Design, ML Fundamentals, Coding. Happy to help anyone preparing! #OpenToWork #MachineLearning",
         "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&q=80",
         "likes": 89, "liked_by": [], "comments": ["Congratulations! 🎊", "Please share tips!", "Inspiring! 💪"], "time": "4h ago"},
        {"id": 3, "user": "Rahul Verma", "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Rahul",
         "text": "📊 Just published my research on LLM fine-tuning for Indian languages. Achieved 94% accuracy on Hindi NLP tasks using LoRA. Paper link in comments! #NLP #DeepLearning #Research",
         "image": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=600&q=80",
         "likes": 156, "liked_by": [], "comments": ["Groundbreaking work!", "Share the paper link!", "🔥🔥🔥"], "time": "6h ago"},
        {"id": 4, "user": "Sneha Patel", "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Sneha",
         "text": "☁️ GCP Professional Data Engineer certified! 3 months of prep, 2 practice exams, and lots of BigQuery queries later — finally got it! #GCP #CloudEngineering #TATA",
         "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80",
         "likes": 73, "liked_by": [], "comments": ["Well deserved! 🏆", "Which resources did you use?"], "time": "1d ago"},
    ]
if "connections" not in st.session_state:
    st.session_state.connections = ["Priya Sharma", "Rahul Verma", "Ankit Gupta"]
if "notifications" not in st.session_state:
    st.session_state.notifications = [
        {"msg": "Priya Sharma liked your post", "time": "1h ago", "read": False},
        {"msg": "Rahul Verma commented: 'Amazing work!'", "time": "3h ago", "read": False},
        {"msg": "New job match: ML Engineer at Google", "time": "5h ago", "read": True},
        {"msg": "Sneha Patel sent you a connection request", "time": "1d ago", "read": True},
    ]

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 0.5rem 0;'>
        <img src='https://img.icons8.com/fluency/96/india.png' width='60'/>
        <h2 style='color:#e8eaf6 !important; margin:0.3rem 0 0 0; font-size:1.3rem;'>FacebookIndia AI</h2>
        <p style='color:#90caf9 !important; font-size:0.8rem; margin:0;'>by Ashu · AI Portal</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    unread = sum(1 for n in st.session_state.notifications if not n["read"])
    notif_label = f"🔔 Notifications  🔴{unread}" if unread else "🔔 Notifications"

    page = st.radio("", [
        "🏠  Home",
        "📰  Feed",
        "👤  My Profile",
        "🌐  Network",
        "💼  Job Search",
        "🤖  AI Chatbot",
        "📚  Knowledge Base",
        "📊  TATA Overview",
        notif_label,
    ])
    st.markdown("---")
    st.markdown("""
    <div style='display:flex; align-items:center; gap:10px; padding:0.5rem;'>
        <img src='https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu' width='40'
             style='border-radius:50%; border:2px solid #1a73e8;'/>
        <div>
            <div style='color:#e8eaf6 !important; font-weight:600; font-size:0.9rem;'>Ashu</div>
            <div style='color:#4caf50 !important; font-size:0.75rem;'>🟢 Online</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Route pages
if "Home" in page:       home.show()
elif "Feed" in page:     feed.show()
elif "Profile" in page:  profile.show()
elif "Network" in page:  network.show()
elif "Job" in page:      jobs.show()
elif "Chatbot" in page:  chatbot.show()
elif "Knowledge" in page: knowledge.show()
elif "TATA" in page:     tata_overview.show()
elif "Notifications" in page:
    st.markdown("## 🔔 Notifications")
    for n in st.session_state.notifications:
        bg = "linear-gradient(90deg,#e8f0fe,#f8f9ff)" if not n["read"] else "white"
        dot = "🔵" if not n["read"] else "⚪"
        st.markdown(f"""
        <div style='background:{bg}; padding:1rem 1.5rem; border-radius:12px;
                    margin-bottom:0.6rem; border-left:4px solid #1a73e8;
                    box-shadow:0 2px 6px rgba(0,0,0,0.06);'>
            <span style='font-size:1rem;'>{dot} {n["msg"]}</span>
            <span style='color:#999; font-size:0.8rem; float:right;'>{n["time"]}</span>
        </div>""", unsafe_allow_html=True)
        n["read"] = True
    if st.button("✅ Mark all as read"):
        st.success("All cleared!")
