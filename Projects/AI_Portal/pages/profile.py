import streamlit as st

def show():
    # Cover photo
    st.markdown("""
    <div style='position:relative; border-radius:20px; overflow:hidden; height:220px; margin-bottom:0;'>
        <img src='https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&q=70'
             style='width:100%; height:100%; object-fit:cover;'/>
        <div style='position:absolute; top:0; left:0; right:0; bottom:0;
                    background:linear-gradient(to bottom, transparent 40%, rgba(13,27,42,0.8));'></div>
        <div style='position:absolute; bottom:1.5rem; left:2rem; color:white;'>
            <h2 style='margin:0; font-size:1.8rem; font-weight:800;'>Ashu</h2>
            <p style='margin:0; color:#90caf9;'>AI & Data Science Engineer · India 🇮🇳</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Avatar + actions
    col1, col2, col3 = st.columns([1, 4, 2])
    with col1:
        st.markdown("""
        <img src='https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu'
             style='width:100px; height:100px; border-radius:50%;
                    border:4px solid white; margin-top:-50px;
                    box-shadow:0 4px 16px rgba(0,0,0,0.2);'/>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='margin-top:0.5rem;'>
            <p style='color:#555; margin:0;'>
                🏢 AI & Data Science Engineer &nbsp;|&nbsp;
                📍 India &nbsp;|&nbsp;
                🔗 <a href='https://github.com/ashu82911' style='color:#1a73e8;'>ashu82911</a>
            </p>
            <p style='color:#777; font-size:0.85rem; margin:4px 0;'>
                Building intelligent systems with ML, Deep Learning & Cloud
            </p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("✏️ Edit Profile")
        st.button("📤 Share Profile")

    st.markdown("---")

    # Stats
    s1, s2, s3, s4 = st.columns(4)
    stats = [
        ("👥", len(st.session_state.connections), "Connections", "#1a73e8"),
        ("📝", len(st.session_state.posts),        "Posts",       "#9c27b0"),
        ("👍", sum(p["likes"] for p in st.session_state.posts), "Likes", "#e65100"),
        ("🏆", "3", "Awards", "#f57c00"),
    ]
    for col, (icon, val, label, color) in zip([s1,s2,s3,s4], stats):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1.2rem; border-radius:14px;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08); text-align:center;
                        border-bottom:3px solid {color};'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:1.8rem; font-weight:800; color:{color};'>{val}</div>
                <div style='color:#777; font-size:0.82rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_r = st.columns([2, 3])

    with col_l:
        # About
        st.markdown("""
        <div style='background:white; padding:1.3rem; border-radius:14px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:1rem;'>
            <h4 style='color:#0d1b2a; margin-top:0;'>📋 About</h4>
            <p style='color:#555; line-height:1.7; font-size:0.9rem;'>
                Passionate AI & Data Science Engineer with expertise in Machine Learning,
                Deep Learning, NLP, and Cloud technologies (GCP, BigQuery, Airflow).
                Building intelligent systems that solve real-world problems.
            </p>
        </div>""", unsafe_allow_html=True)

        # Skills
        skills = [("Python","#1a73e8"),("Machine Learning","#9c27b0"),("Deep Learning","#e65100"),
                  ("NLP","#00897b"),("GCP","#f57c00"),("BigQuery","#1565c0"),
                  ("Airflow","#2e7d32"),("Streamlit","#ff5722"),("TensorFlow","#ff6f00"),("PyTorch","#e53935")]
        badges = "".join([
            f"<span style='background:{c}22; color:{c}; padding:5px 12px; border-radius:20px; "
            f"font-size:0.8rem; font-weight:600; margin:3px; display:inline-block; border:1px solid {c}44;'>{s}</span>"
            for s, c in skills])
        st.markdown(f"""
        <div style='background:white; padding:1.3rem; border-radius:14px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:1rem;'>
            <h4 style='color:#0d1b2a; margin-top:0;'>🛠️ Skills</h4>
            {badges}
        </div>""", unsafe_allow_html=True)

        # Projects
        projects = [
            ("FacebookIndia AI Portal","Streamlit","https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=300&q=60"),
            ("Stock TimeSeries Forecasting","Python/LSTM","https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=300&q=60"),
            ("Face Emotion Detection","CNN/Keras","https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&q=60"),
        ]
        st.markdown("""
        <div style='background:white; padding:1.3rem; border-radius:14px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08);'>
            <h4 style='color:#0d1b2a; margin-top:0;'>🚀 Projects</h4>
        </div>""", unsafe_allow_html=True)
        for pname, tech, img in projects:
            st.markdown(f"""
            <div style='display:flex; gap:10px; align-items:center; margin:8px 0;
                        background:#f8f9fa; border-radius:10px; overflow:hidden;'>
                <img src='{img}' style='width:60px; height:60px; object-fit:cover;'/>
                <div style='padding:0.4rem;'>
                    <div style='font-weight:600; color:#0d1b2a; font-size:0.88rem;'>{pname}</div>
                    <div style='color:#1a73e8; font-size:0.78rem;'>{tech}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    with col_r:
        # My Posts
        st.markdown("""
        <div style='background:white; padding:1.3rem; border-radius:14px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08);'>
            <h4 style='color:#0d1b2a; margin-top:0;'>📝 My Posts</h4>
        </div>""", unsafe_allow_html=True)
        my_posts = [p for p in st.session_state.posts if p["user"] == "Ashu"]
        for post in my_posts:
            img_html = f"<img src='{post['image']}' style='width:100%; height:160px; object-fit:cover; border-radius:10px; margin:6px 0;'/>" if post.get("image") else ""
            st.markdown(f"""
            <div style='background:#f8f9fa; border-radius:12px; padding:1rem;
                        margin:0.6rem 0; border-left:4px solid #1a73e8;'>
                {img_html}
                <p style='margin:0; color:#333; font-size:0.9rem;'>{post["text"][:120]}...</p>
                <div style='color:#999; font-size:0.78rem; margin-top:6px;'>
                    👍 {post["likes"]} · 💬 {len(post["comments"])} · {post["time"]}
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("✏️ Edit Profile"):
        st.text_input("Display Name", value="Ashu")
        st.text_area("Bio", value="AI & Data Science Engineer passionate about building intelligent systems.")
        st.text_input("Location", value="India")
        st.text_input("GitHub", value="ashu82911")
        if st.button("💾 Save Profile"):
            st.success("Profile updated!")
            st.balloons()
