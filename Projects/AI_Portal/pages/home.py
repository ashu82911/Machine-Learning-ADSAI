import streamlit as st

def show():
    # Hero Banner
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0a0f1e 0%, #1a237e 50%, #1a73e8 100%);
                padding: 3.5rem 2rem; border-radius: 20px; text-align: center;
                margin-bottom: 2rem; position:relative; overflow:hidden;'>
        <img src='https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&q=60'
             style='position:absolute;top:0;left:0;width:100%;height:100%;
                    object-fit:cover;opacity:0.15;border-radius:20px;'/>
        <div style='position:relative;'>
            <img src='https://img.icons8.com/fluency/96/india.png' width='70'/>
            <h1 style='color:white; font-size:3rem; margin:0.5rem 0; font-weight:800;
                       text-shadow:0 2px 20px rgba(0,0,0,0.5);'>🇮🇳 FacebookIndia AI</h1>
            <p style='color:#90caf9; font-size:1.15rem; margin:0;'>
                India's AI-powered Social Portal · Jobs · Chatbot · Knowledge · Network
            </p>
            <div style='margin-top:1.5rem;'>
                <span style='background:rgba(255,255,255,0.15); color:white; padding:6px 16px;
                             border-radius:20px; font-size:0.85rem; margin:4px;
                             backdrop-filter:blur(10px); display:inline-block;'>🤖 AI Chatbot</span>
                <span style='background:rgba(255,255,255,0.15); color:white; padding:6px 16px;
                             border-radius:20px; font-size:0.85rem; margin:4px;
                             backdrop-filter:blur(10px); display:inline-block;'>💼 Job Search</span>
                <span style='background:rgba(255,255,255,0.15); color:white; padding:6px 16px;
                             border-radius:20px; font-size:0.85rem; margin:4px;
                             backdrop-filter:blur(10px); display:inline-block;'>🌐 Network</span>
                <span style='background:rgba(255,255,255,0.15); color:white; padding:6px 16px;
                             border-radius:20px; font-size:0.85rem; margin:4px;
                             backdrop-filter:blur(10px); display:inline-block;'>📚 Knowledge</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature cards row 1
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&q=70",
         "📰", "Feed", "#1a73e8", "Share posts, like, comment & connect"),
        ("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=70",
         "👤", "My Profile", "#9c27b0", "Your AI professional profile"),
        ("https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&q=70",
         "🌐", "Network", "#00897b", "Connect with AI/ML professionals"),
        ("https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=400&q=70",
         "💼", "Job Search", "#e65100", "Browse AI/ML/Cloud jobs"),
    ]
    for col, (img, icon, title, color, desc) in zip([c1,c2,c3,c4], cards):
        with col:
            st.markdown(f"""
            <div style='background:white; border-radius:16px; overflow:hidden;
                        box-shadow:0 4px 16px rgba(0,0,0,0.1); margin-bottom:1rem;
                        transition:transform 0.2s;'>
                <img src='{img}' style='width:100%; height:120px; object-fit:cover;'/>
                <div style='padding:1rem; border-top:3px solid {color};'>
                    <div style='font-size:1.5rem;'>{icon}</div>
                    <h4 style='color:{color}; margin:0.3rem 0; font-size:1rem;'>{title}</h4>
                    <p style='color:#666; font-size:0.8rem; margin:0;'>{desc}</p>
                </div>
            </div>""", unsafe_allow_html=True)

    # Feature cards row 2
    c5, c6, c7, c8 = st.columns(4)
    cards2 = [
        ("https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=400&q=70",
         "🤖", "AI Chatbot", "#1565c0", "AshBot answers tech & career Qs"),
        ("https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400&q=70",
         "📚", "Knowledge Base", "#2e7d32", "ML, DL, DS, Cloud learning"),
        ("https://images.unsplash.com/photo-1568952433726-3896e3881c65?w=400&q=70",
         "📊", "TATA Overview", "#0d47a1", "Cloud Data Engineering insights"),
        ("https://images.unsplash.com/photo-1614680376573-df3480f0c6ff?w=400&q=70",
         "🔔", "Notifications", "#f57c00", "Likes, comments & job alerts"),
    ]
    for col, (img, icon, title, color, desc) in zip([c5,c6,c7,c8], cards2):
        with col:
            st.markdown(f"""
            <div style='background:white; border-radius:16px; overflow:hidden;
                        box-shadow:0 4px 16px rgba(0,0,0,0.1); margin-bottom:1rem;'>
                <img src='{img}' style='width:100%; height:120px; object-fit:cover;'/>
                <div style='padding:1rem; border-top:3px solid {color};'>
                    <div style='font-size:1.5rem;'>{icon}</div>
                    <h4 style='color:{color}; margin:0.3rem 0; font-size:1rem;'>{title}</h4>
                    <p style='color:#666; font-size:0.8rem; margin:0;'>{desc}</p>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Activity stats
    st.markdown("### 📊 Your Activity")
    a1, a2, a3, a4 = st.columns(4)
    stats = [
        ("👥", len(st.session_state.get("connections",[])), "Connections", "#1a73e8"),
        ("📝", len(st.session_state.get("posts",[])),       "Posts",       "#9c27b0"),
        ("👍", sum(p["likes"] for p in st.session_state.get("posts",[])), "Likes", "#e65100"),
        ("🔔", sum(1 for n in st.session_state.get("notifications",[]) if not n["read"]), "Unread", "#f57c00"),
    ]
    for col, (icon, val, label, color) in zip([a1,a2,a3,a4], stats):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1.2rem; border-radius:14px;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08); text-align:center;
                        border-bottom:3px solid {color};'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:2rem; font-weight:800; color:{color};'>{val}</div>
                <div style='color:#777; font-size:0.85rem; font-weight:500;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Trending topics
    st.markdown("### 🔥 Trending in AI India")
    t1, t2, t3 = st.columns(3)
    trends = [
        ("https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=500&q=70",
         "Large Language Models", "12.4K posts", "#1a73e8"),
        ("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=70",
         "Data Engineering India", "8.7K posts", "#9c27b0"),
        ("https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=500&q=70",
         "AI Jobs 2025", "15.2K posts", "#e65100"),
    ]
    for col, (img, topic, count, color) in zip([t1,t2,t3], trends):
        with col:
            st.markdown(f"""
            <div style='background:white; border-radius:14px; overflow:hidden;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08);'>
                <img src='{img}' style='width:100%; height:140px; object-fit:cover;'/>
                <div style='padding:0.8rem 1rem;'>
                    <div style='font-weight:700; color:#0d1b2a; font-size:0.95rem;'>{topic}</div>
                    <div style='color:{color}; font-size:0.8rem; font-weight:600;'>{count}</div>
                </div>
            </div>""", unsafe_allow_html=True)
