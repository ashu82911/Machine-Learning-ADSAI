import streamlit as st

def show():
    col_feed, col_right = st.columns([3, 1])

    with col_feed:
        st.markdown("## 📰 Feed")

        # Create Post box
        st.markdown("""
        <div style='background:white; padding:1.2rem 1.5rem; border-radius:16px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:1.2rem;'>
            <div style='display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;'>
                <img src='https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu'
                     width='44' style='border-radius:50%; border:2px solid #1a73e8;'/>
                <span style='color:#555; font-size:0.95rem;'>What's on your mind, Ashu?</span>
            </div>
        </div>""", unsafe_allow_html=True)

        new_post = st.text_area("", placeholder="Share something with the AI community...",
                                label_visibility="collapsed", height=90)
        img_url = st.text_input("📷 Add image URL (optional)",
                                placeholder="https://images.unsplash.com/...",
                                label_visibility="visible")

        ca, cb, cc = st.columns([2, 2, 6])
        with ca: st.button("😊 Feeling")
        with cb: st.button("📍 Location")
        with cc:
            if st.button("🚀 Post Now", type="primary"):
                if new_post.strip():
                    new_id = max([p["id"] for p in st.session_state.posts], default=0) + 1
                    st.session_state.posts.insert(0, {
                        "id": new_id, "user": "Ashu",
                        "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu",
                        "text": new_post,
                        "image": img_url if img_url.strip() else "",
                        "likes": 0, "liked_by": [], "comments": [], "time": "Just now"
                    })
                    st.success("✅ Post shared!")
                    st.rerun()
                else:
                    st.warning("Write something first!")

        st.markdown("---")

        # Stories
        st.markdown("**📖 Stories**")
        stories = [
            ("Ashu",  "https://api.dicebear.com/7.x/avataaars/svg?seed=Ashu",
             "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=200&q=60", "#1a73e8"),
            ("Priya", "https://api.dicebear.com/7.x/avataaars/svg?seed=Priya",
             "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&q=60", "#e91e63"),
            ("Rahul", "https://api.dicebear.com/7.x/avataaars/svg?seed=Rahul",
             "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=200&q=60", "#9c27b0"),
            ("Sneha", "https://api.dicebear.com/7.x/avataaars/svg?seed=Sneha",
             "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=200&q=60", "#ff5722"),
            ("Amit",  "https://api.dicebear.com/7.x/avataaars/svg?seed=Amit",
             "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=200&q=60", "#4caf50"),
        ]
        s_cols = st.columns(5)
        for col, (name, av, bg, color) in zip(s_cols, stories):
            with col:
                st.markdown(f"""
                <div style='border-radius:14px; overflow:hidden; cursor:pointer;
                            box-shadow:0 3px 10px rgba(0,0,0,0.12); position:relative; height:130px;'>
                    <img src='{bg}' style='width:100%; height:100%; object-fit:cover;'/>
                    <div style='position:absolute; top:0; left:0; right:0; bottom:0;
                                background:linear-gradient(to bottom, transparent 40%, rgba(0,0,0,0.6));'></div>
                    <img src='{av}' width='36' style='position:absolute; top:8px; left:8px;
                         border-radius:50%; border:3px solid {color};'/>
                    <div style='position:absolute; bottom:8px; left:8px; color:white;
                                font-size:0.75rem; font-weight:600;'>{name}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Posts
        for post in st.session_state.posts:
            st.markdown(f"""
            <div style='background:white; border-radius:16px; overflow:hidden;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:1.2rem;'>
                <div style='padding:1.2rem 1.5rem 0.8rem;'>
                    <div style='display:flex; align-items:center; gap:12px;'>
                        <img src='{post["avatar"]}' width='46'
                             style='border-radius:50%; border:2px solid #1a73e8;'/>
                        <div>
                            <div style='font-weight:700; color:#0d1b2a;'>{post["user"]}</div>
                            <div style='color:#999; font-size:0.78rem;'>{post["time"]} · 🌐 Public</div>
                        </div>
                    </div>
                    <p style='color:#333; margin:0.8rem 0; line-height:1.65; font-size:0.95rem;'>
                        {post["text"]}
                    </p>
                </div>""", unsafe_allow_html=True)

            if post.get("image"):
                st.markdown(f"""
                <img src='{post["image"]}' style='width:100%; max-height:380px;
                     object-fit:cover; display:block;'/>""", unsafe_allow_html=True)

            liked = "Ashu" in post["liked_by"]
            st.markdown(f"""
            <div style='padding:0.5rem 1.5rem; border-top:1px solid #f0f0f0;
                        display:flex; gap:8px; color:#666; font-size:0.85rem;'>
                <span>👍 {post["likes"]} likes</span>
                <span>·</span>
                <span>💬 {len(post["comments"])} comments</span>
            </div>
            </div>""", unsafe_allow_html=True)

            bc1, bc2, bc3 = st.columns(3)
            with bc1:
                like_label = "💙 Liked" if liked else "👍 Like"
                if st.button(like_label, key=f"like_{post['id']}"):
                    if "Ashu" not in post["liked_by"]:
                        post["likes"] += 1
                        post["liked_by"].append("Ashu")
                    else:
                        post["likes"] -= 1
                        post["liked_by"].remove("Ashu")
                    st.rerun()
            with bc2:
                st.button(f"💬 Comment", key=f"cmt_btn_{post['id']}")
            with bc3:
                st.button("↗️ Share", key=f"share_{post['id']}")

            # Comments
            for c in post["comments"]:
                st.markdown(f"""
                <div style='background:#f8f9fa; border-radius:10px; padding:0.5rem 1rem;
                            margin:0.2rem 1.5rem; font-size:0.88rem; color:#444;'>
                    💬 {c}
                </div>""", unsafe_allow_html=True)

            new_c = st.text_input("", placeholder="Write a comment...",
                                  key=f"cinput_{post['id']}", label_visibility="collapsed")
            if st.button("Send 📤", key=f"csend_{post['id']}"):
                if new_c.strip():
                    post["comments"].append(f"Ashu: {new_c}")
                    st.rerun()

    # Right sidebar
    with col_right:
        st.markdown("""
        <div style='background:white; border-radius:14px; padding:1rem;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-bottom:1rem;'>
            <h4 style='color:#0d1b2a; margin-top:0;'>🔥 Trending Topics</h4>
        </div>""", unsafe_allow_html=True)
        trends = ["#LLM", "#AIIndia", "#DataScience", "#MLOps", "#GCP", "#DeepLearning", "#Python"]
        for t in trends:
            st.markdown(f"""
            <div style='background:#e8f0fe; color:#1a73e8; padding:6px 12px;
                        border-radius:20px; margin:4px 0; font-size:0.85rem;
                        font-weight:600; cursor:pointer;'>{t}</div>""",
                        unsafe_allow_html=True)

        st.markdown("""
        <div style='background:white; border-radius:14px; padding:1rem;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08); margin-top:1rem;'>
            <h4 style='color:#0d1b2a; margin-top:0;'>👥 Suggested</h4>
        </div>""", unsafe_allow_html=True)
        suggested = [("Vikram Singh","AI Researcher","https://api.dicebear.com/7.x/avataaars/svg?seed=Vikram"),
                     ("Neha Joshi","DL Engineer","https://api.dicebear.com/7.x/avataaars/svg?seed=Neha")]
        for name, role, av in suggested:
            st.markdown(f"""
            <div style='display:flex; align-items:center; gap:8px; margin:8px 0;'>
                <img src='{av}' width='36' style='border-radius:50%;'/>
                <div>
                    <div style='font-weight:600; font-size:0.85rem; color:#0d1b2a;'>{name}</div>
                    <div style='color:#777; font-size:0.75rem;'>{role}</div>
                </div>
            </div>""", unsafe_allow_html=True)
            st.button("➕ Connect", key=f"sug_{name}")
