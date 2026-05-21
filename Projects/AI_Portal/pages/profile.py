import streamlit as st

def show():
    # Cover photo
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0d1b2a, #1a73e8);
                height: 180px; border-radius: 14px; margin-bottom: 0;'></div>
    """, unsafe_allow_html=True)

    # Profile header
    col1, col2, col3 = st.columns([1, 3, 2])
    with col1:
        st.markdown("""
        <div style='background:white; border-radius:50%; width:100px; height:100px;
                    display:flex; align-items:center; justify-content:center;
                    font-size:3.5rem; margin-top:-50px; border:4px solid white;
                    box-shadow:0 2px 8px rgba(0,0,0,0.15);'>
            👨‍💻
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='margin-top:0.5rem;'>
            <h2 style='margin:0; color:#0d1b2a;'>Ashu</h2>
            <p style='color:#555; margin:2px 0;'>AI & Data Science Engineer</p>
            <p style='color:#1a73e8; font-size:0.9rem;'>📍 India &nbsp;|&nbsp; 🌐 ashu82911</p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("✏️ Edit Profile")
        st.button("➕ Add to Story")

    st.markdown("---")

    # Stats row
    s1, s2, s3, s4 = st.columns(4)
    stats = [("👥", str(len(st.session_state.connections)), "Connections"),
             ("📝", str(len(st.session_state.posts)), "Posts"),
             ("👍", str(sum(p["likes"] for p in st.session_state.posts)), "Total Likes"),
             ("🏆", "3", "Achievements")]
    for col, (icon, val, label) in zip([s1, s2, s3, s4], stats):
        with col:
            st.markdown(f"""
            <div style='background:white; padding:1rem; border-radius:12px;
                        text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.07);'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:1.5rem; font-weight:700; color:#1a73e8;'>{val}</div>
                <div style='color:#777; font-size:0.85rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 3])

    with col_left:
        # About
        st.markdown("""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07); margin-bottom:1rem;'>
            <h4 style='color:#0d1b2a; margin-top:0;'>📋 About</h4>
            <p style='color:#555; line-height:1.7;'>
                AI & Data Science Engineer passionate about building intelligent systems.
                Experienced in ML, Deep Learning, NLP, and Cloud technologies.
            </p>
        </div>""", unsafe_allow_html=True)

        # Skills
        skills = ["Python", "Machine Learning", "Deep Learning", "NLP",
                  "GCP", "BigQuery", "Airflow", "Streamlit", "TensorFlow", "PyTorch"]
        skills_html = "".join([
            f"<span style='background:#e8f0fe; color:#1a73e8; padding:4px 10px; "
            f"border-radius:20px; font-size:0.8rem; margin:3px; display:inline-block;'>{s}</span>"
            for s in skills
        ])
        st.markdown(f"""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07);'>
            <h4 style='color:#0d1b2a; margin-top:0;'>🛠️ Skills</h4>
            {skills_html}
        </div>""", unsafe_allow_html=True)

    with col_right:
        # My Posts
        st.markdown("""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07);'>
            <h4 style='color:#0d1b2a; margin-top:0;'>📝 My Posts</h4>
        </div>""", unsafe_allow_html=True)

        my_posts = [p for p in st.session_state.posts if p["user"] == "Ashu"]
        if my_posts:
            for post in my_posts:
                st.markdown(f"""
                <div style='background:#f8f9fa; border-radius:10px; padding:0.8rem 1rem;
                            margin:0.5rem 0; border-left:4px solid #1a73e8;'>
                    <p style='margin:0; color:#333;'>{post["text"]}</p>
                    <span style='color:#999; font-size:0.8rem;'>
                        👍 {post["likes"]} likes · 💬 {len(post["comments"])} comments · {post["time"]}
                    </span>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No posts yet. Share something on the Feed!")

    st.markdown("<br>", unsafe_allow_html=True)

    # Edit profile form
    with st.expander("✏️ Edit Profile Info"):
        new_name = st.text_input("Display Name", value="Ashu")
        new_bio = st.text_area("Bio", value="AI & Data Science Engineer passionate about building intelligent systems.")
        new_loc = st.text_input("Location", value="India")
        new_skills = st.text_input("Skills (comma separated)", value="Python, ML, Deep Learning, GCP")
        if st.button("💾 Save Profile"):
            st.success("Profile updated successfully!")
