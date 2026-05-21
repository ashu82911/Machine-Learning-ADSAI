import streamlit as st
from pages import home, jobs, chatbot, knowledge, tata_overview, feed, profile, network

st.set_page_config(
    page_title="Ashu | AI Portal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0d1b2a 0%, #1b2a4a 100%); }
    [data-testid="stSidebar"] * { color: #e0e0e0 !important; }
    .main { background-color: #f0f2f5; }
    .stButton>button {
        background: linear-gradient(90deg, #1a73e8, #0d47a1);
        color: white; border-radius: 8px; border: none;
        padding: 0.5rem 1.5rem; font-weight: 600;
    }
    .stButton>button:hover { background: linear-gradient(90deg, #0d47a1, #1a73e8); }
    h1, h2, h3 { color: #0d1b2a; }
    div[data-testid="stChatMessage"] { background: white; border-radius: 12px; margin: 4px 0; }
</style>
""", unsafe_allow_html=True)

# Session state defaults
if "username" not in st.session_state:
    st.session_state.username = "Ashu"
if "posts" not in st.session_state:
    st.session_state.posts = [
        {"id": 1, "user": "Ashu", "avatar": "👨‍💻", "text": "Just deployed my AI Portal! 🚀 Built with Streamlit + Python.", "likes": 12, "liked_by": [], "comments": ["Amazing work!", "Congrats 🎉"], "time": "2h ago"},
        {"id": 2, "user": "Priya Sharma", "avatar": "👩‍💼", "text": "Looking for ML Engineer roles in Bangalore. Open to opportunities! #OpenToWork #MachineLearning", "likes": 8, "liked_by": [], "comments": ["Best of luck!", "Check out TCS openings"], "time": "4h ago"},
        {"id": 3, "user": "Rahul Verma", "avatar": "👨‍🔬", "text": "Just completed my Deep Learning certification from Coursera. Feeling great! 🧠 #DeepLearning #AI", "likes": 24, "liked_by": [], "comments": ["Well done!", "Which course?"], "time": "6h ago"},
    ]
if "connections" not in st.session_state:
    st.session_state.connections = ["Priya Sharma", "Rahul Verma", "Ankit Gupta"]
if "notifications" not in st.session_state:
    st.session_state.notifications = [
        {"msg": "Priya Sharma liked your post", "time": "1h ago", "read": False},
        {"msg": "Rahul Verma commented on your post", "time": "3h ago", "read": False},
        {"msg": "New job match: ML Engineer at Google", "time": "5h ago", "read": True},
    ]

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=70)
    st.markdown(f"## 👨‍💻 Ashu's AI Portal")
    st.markdown("---")

    unread = sum(1 for n in st.session_state.notifications if not n["read"])
    notif_label = f"🔔 Notifications ({unread})" if unread else "🔔 Notifications"

    page = st.radio("Navigate", [
        "🏠 Home",
        "📰 Feed",
        "👤 My Profile",
        "🌐 Network",
        "💼 Job Search",
        "🤖 AI Chatbot",
        "📚 Knowledge Base",
        "📊 TATA Overview",
        notif_label,
    ])
    st.markdown("---")
    st.markdown("**Ashu** · ashu82911")
    st.markdown("🟢 Online")

# Route pages
if page == "🏠 Home":
    home.show()
elif page == "📰 Feed":
    feed.show()
elif page == "👤 My Profile":
    profile.show()
elif page == "🌐 Network":
    network.show()
elif page == "💼 Job Search":
    jobs.show()
elif page == "🤖 AI Chatbot":
    chatbot.show()
elif page == "📚 Knowledge Base":
    knowledge.show()
elif page == "📊 TATA Overview":
    tata_overview.show()
elif "Notifications" in page:
    st.markdown("## 🔔 Notifications")
    for n in st.session_state.notifications:
        n["read"] = True
        bg = "#e8f0fe" if not n["read"] else "white"
        st.markdown(f"""
        <div style='background:{bg}; padding:0.8rem 1.2rem; border-radius:10px;
                    margin-bottom:0.5rem; border-left:4px solid #1a73e8;'>
            <span style='color:#0d1b2a;'>{n["msg"]}</span>
            <span style='color:#999; font-size:0.8rem; float:right;'>{n["time"]}</span>
        </div>""", unsafe_allow_html=True)
    if st.button("Mark all as read"):
        for n in st.session_state.notifications:
            n["read"] = True
        st.success("All notifications marked as read!")
