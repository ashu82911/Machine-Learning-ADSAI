import streamlit as st
import time

def show():
    st.markdown("## 📰 Feed")

    # ── Create Post ──────────────────────────────────────────────
    st.markdown("""
    <div style='background:white; padding:1rem 1.5rem; border-radius:14px;
                box-shadow:0 2px 8px rgba(0,0,0,0.07); margin-bottom:1.2rem;'>
        <h4 style='margin:0 0 0.5rem 0; color:#0d1b2a;'>✍️ Create Post</h4>
    </div>""", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([1, 10])
        with col1:
            st.markdown("<div style='font-size:2rem; margin-top:0.3rem;'>👨‍💻</div>", unsafe_allow_html=True)
        with col2:
            new_post = st.text_area("", placeholder="What's on your mind, Ashu?", label_visibility="collapsed", height=80)

        col_a, col_b, col_c, col_d = st.columns([2, 2, 2, 4])
        with col_a:
            photo = st.button("📷 Photo")
        with col_b:
            video = st.button("🎥 Video")
        with col_c:
            feeling = st.button("😊 Feeling")
        with col_d:
            if st.button("🚀 Post", type="primary"):
                if new_post.strip():
                    new_id = max([p["id"] for p in st.session_state.posts], default=0) + 1
                    st.session_state.posts.insert(0, {
                        "id": new_id, "user": "Ashu", "avatar": "👨‍💻",
                        "text": new_post, "likes": 0, "liked_by": [],
                        "comments": [], "time": "Just now"
                    })
                    st.success("Post shared!")
                    st.rerun()
                else:
                    st.warning("Write something first!")

    st.markdown("---")

    # ── Stories Row ──────────────────────────────────────────────
    st.markdown("**📖 Stories**")
    s_cols = st.columns(5)
    stories = [
        ("👨‍💻", "Ashu", "#1a73e8"),
        ("👩‍💼", "Priya", "#e91e63"),
        ("👨‍🔬", "Rahul", "#9c27b0"),
        ("👩‍💻", "Sneha", "#ff5722"),
        ("👨‍🎓", "Amit", "#4caf50"),
    ]
    for col, (avatar, name, color) in zip(s_cols, stories):
        with col:
            st.markdown(f"""
            <div style='background:white; border-radius:12px; padding:0.8rem;
                        text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08);
                        border-top: 4px solid {color}; cursor:pointer;'>
                <div style='font-size:2rem;'>{avatar}</div>
                <div style='font-size:0.75rem; color:#555; margin-top:4px;'>{name}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Posts Feed ───────────────────────────────────────────────
    for post in st.session_state.posts:
        with st.container():
            st.markdown(f"""
            <div style='background:white; border-radius:14px; padding:1.2rem 1.5rem;
                        box-shadow:0 2px 8px rgba(0,0,0,0.07); margin-bottom:1rem;'>
                <div style='display:flex; align-items:center; margin-bottom:0.8rem;'>
                    <span style='font-size:2rem; margin-right:0.8rem;'>{post["avatar"]}</span>
                    <div>
                        <strong style='color:#0d1b2a;'>{post["user"]}</strong><br>
                        <span style='color:#999; font-size:0.8rem;'>{post["time"]}</span>
                    </div>
                </div>
                <p style='color:#333; margin:0 0 1rem 0; line-height:1.6;'>{post["text"]}</p>
                <hr style='border:none; border-top:1px solid #f0f0f0; margin:0.5rem 0;'>
            </div>""", unsafe_allow_html=True)

            # Action buttons
            c1, c2, c3, c4 = st.columns([2, 2, 2, 4])
            liked = "Ashu" in post["liked_by"]
            like_label = f"👍 Like ({post['likes']})" if not liked else f"💙 Liked ({post['likes']})"

            with c1:
                if st.button(like_label, key=f"like_{post['id']}"):
                    if "Ashu" not in post["liked_by"]:
                        post["likes"] += 1
                        post["liked_by"].append("Ashu")
                    else:
                        post["likes"] -= 1
                        post["liked_by"].remove("Ashu")
                    st.rerun()
            with c2:
                show_comments = st.button(f"💬 Comment ({len(post['comments'])})", key=f"cmt_{post['id']}")
            with c3:
                st.button("↗️ Share", key=f"share_{post['id']}")

            # Comments section
            if show_comments or f"show_cmt_{post['id']}" in st.session_state:
                st.session_state[f"show_cmt_{post['id']}"] = True
                for c in post["comments"]:
                    st.markdown(f"""
                    <div style='background:#f0f2f5; border-radius:8px; padding:0.5rem 1rem;
                                margin:0.3rem 0; font-size:0.9rem; color:#333;'>
                        💬 {c}
                    </div>""", unsafe_allow_html=True)
                new_comment = st.text_input("Write a comment...", key=f"cinput_{post['id']}", label_visibility="collapsed")
                if st.button("Send", key=f"csend_{post['id']}"):
                    if new_comment.strip():
                        post["comments"].append(f"Ashu: {new_comment}")
                        st.rerun()
