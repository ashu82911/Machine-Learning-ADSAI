import streamlit as st

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0d1b2a 0%, #1a73e8 100%);
                padding: 3rem; border-radius: 16px; text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: white; font-size: 2.8rem; margin: 0;'>🤖 Ashu's AI Portal</h1>
        <p style='color: #cce0ff; font-size: 1.1rem; margin-top: 0.8rem;'>
            AI-powered Job Search · Social Feed · Chatbot · Knowledge Base
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Feature cards — row 1
    col1, col2, col3, col4 = st.columns(4)
    cards = [
        ("📰", "Feed",          "#1a73e8", "Share posts, like, comment & connect with peers"),
        ("👤", "My Profile",    "#9c27b0", "Your personal AI professional profile page"),
        ("🌐", "Network",       "#00897b", "Connect with AI/ML professionals & grow network"),
        ("💼", "Job Search",    "#e65100", "Browse AI/ML/Cloud jobs with smart filters"),
    ]
    for col, (icon, title, color, desc) in zip([col1, col2, col3, col4], cards):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1.4rem; border-radius:12px;
                        box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;
                        border-top: 4px solid {color};'>
                <div style='font-size:2.2rem;'>{icon}</div>
                <h4 style='color:{color}; margin:0.4rem 0;'>{title}</h4>
                <p style='color:#666; font-size:0.85rem; margin:0;'>{desc}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature cards — row 2
    col5, col6, col7, col8 = st.columns(4)
    cards2 = [
        ("🤖", "AI Chatbot",      "#1565c0", "AshBot answers AI/ML & career questions"),
        ("📚", "Knowledge Base",  "#2e7d32", "Structured ML, DL, DS, Cloud learning"),
        ("📊", "TATA Overview",   "#0d47a1", "Editable Cloud Data Engineering overview"),
        ("🔔", "Notifications",   "#f57c00", "Stay updated with likes, comments & jobs"),
    ]
    for col, (icon, title, color, desc) in zip([col5, col6, col7, col8], cards2):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1.4rem; border-radius:12px;
                        box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;
                        border-top: 4px solid {color};'>
                <div style='font-size:2.2rem;'>{icon}</div>
                <h4 style='color:{color}; margin:0.4rem 0;'>{title}</h4>
                <p style='color:#666; font-size:0.85rem; margin:0;'>{desc}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick stats
    st.markdown("### 📊 Your Activity")
    a1, a2, a3, a4 = st.columns(4)
    stats = [
        ("👥", len(st.session_state.get("connections", [])), "Connections"),
        ("📝", len(st.session_state.get("posts", [])),       "Posts"),
        ("👍", sum(p["likes"] for p in st.session_state.get("posts", [])), "Likes"),
        ("🔔", sum(1 for n in st.session_state.get("notifications", []) if not n["read"]), "Unread"),
    ]
    for col, (icon, val, label) in zip([a1, a2, a3, a4], stats):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1rem; border-radius:12px;
                        box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;'>
                <div style='font-size:1.6rem;'>{icon}</div>
                <div style='font-size:1.8rem; font-weight:700; color:#1a73e8;'>{val}</div>
                <div style='color:#777; font-size:0.85rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)
