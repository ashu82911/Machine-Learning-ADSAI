import streamlit as st

SUGGESTED = [
    {"name": "Ankit Gupta",    "avatar": "👨‍💻", "role": "Data Scientist @ Microsoft",       "mutual": 5},
    {"name": "Sneha Patel",    "avatar": "👩‍💻", "role": "ML Engineer @ Amazon",             "mutual": 3},
    {"name": "Vikram Singh",   "avatar": "👨‍🔬", "role": "AI Researcher @ IIT Delhi",        "mutual": 7},
    {"name": "Neha Joshi",     "avatar": "👩‍🎓", "role": "Deep Learning Engineer @ Infosys", "mutual": 2},
    {"name": "Rohan Mehta",    "avatar": "👨‍🏫", "role": "NLP Engineer @ Flipkart",          "mutual": 4},
    {"name": "Divya Sharma",   "avatar": "👩‍🔬", "role": "Cloud Architect @ TCS",            "mutual": 6},
]

def show():
    st.markdown("## 🌐 My Network")

    # Stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;'>
            <div style='font-size:2rem;'>👥</div>
            <div style='font-size:2rem; font-weight:700; color:#1a73e8;'>
                {len(st.session_state.connections)}
            </div>
            <div style='color:#777;'>Connections</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;'>
            <div style='font-size:2rem;'>👁️</div>
            <div style='font-size:2rem; font-weight:700; color:#1a73e8;'>48</div>
            <div style='color:#777;'>Profile Views</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div style='background:white; padding:1.2rem; border-radius:12px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;'>
            <div style='font-size:2rem;'>📨</div>
            <div style='font-size:2rem; font-weight:700; color:#1a73e8;'>3</div>
            <div style='color:#777;'>Pending Requests</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Search
    search = st.text_input("🔍 Search people", placeholder="Search by name or role...")

    # ── My Connections ───────────────────────────────────────────
    st.markdown("### 👥 My Connections")
    conn_list = st.session_state.connections
    if search:
        conn_list = [c for c in conn_list if search.lower() in c.lower()]

    if conn_list:
        cols = st.columns(3)
        avatars = ["👩‍💼", "👨‍🔬", "👩‍💻", "👨‍🎓", "👩‍🔬"]
        for i, name in enumerate(conn_list):
            with cols[i % 3]:
                st.markdown(f"""
                <div style='background:white; padding:1rem; border-radius:12px;
                            box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;
                            margin-bottom:0.8rem;'>
                    <div style='font-size:2.5rem;'>{avatars[i % len(avatars)]}</div>
                    <div style='font-weight:600; color:#0d1b2a;'>{name}</div>
                    <div style='color:#1a73e8; font-size:0.8rem;'>Connected ✅</div>
                </div>""", unsafe_allow_html=True)
                if st.button("Remove", key=f"rem_{i}"):
                    st.session_state.connections.remove(name)
                    st.rerun()
    else:
        st.info("No connections found.")

    st.markdown("---")

    # ── Pending Requests ─────────────────────────────────────────
    st.markdown("### 📨 Pending Requests")
    pending = [
        {"name": "Karan Malhotra", "avatar": "👨‍💼", "role": "Data Engineer @ Wipro",    "mutual": 2},
        {"name": "Pooja Nair",     "avatar": "👩‍🏫", "role": "AI Trainer @ BYJU'S",      "mutual": 1},
        {"name": "Suresh Kumar",   "avatar": "👨‍🎓", "role": "ML Intern @ Zoho",         "mutual": 3},
    ]
    p_cols = st.columns(3)
    for i, p in enumerate(pending):
        with p_cols[i % 3]:
            st.markdown(f"""
            <div style='background:white; padding:1rem; border-radius:12px;
                        box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;
                        margin-bottom:0.8rem;'>
                <div style='font-size:2.5rem;'>{p["avatar"]}</div>
                <div style='font-weight:600; color:#0d1b2a;'>{p["name"]}</div>
                <div style='color:#555; font-size:0.8rem;'>{p["role"]}</div>
                <div style='color:#999; font-size:0.75rem;'>{p["mutual"]} mutual connections</div>
            </div>""", unsafe_allow_html=True)
            ca, cb = st.columns(2)
            with ca:
                if st.button("✅ Accept", key=f"acc_{i}"):
                    st.session_state.connections.append(p["name"])
                    st.success(f"Connected with {p['name']}!")
                    st.rerun()
            with cb:
                if st.button("❌ Decline", key=f"dec_{i}"):
                    st.info("Request declined.")

    st.markdown("---")

    # ── People You May Know ──────────────────────────────────────
    st.markdown("### 💡 People You May Know")
    filtered = [p for p in SUGGESTED
                if p["name"] not in st.session_state.connections
                and (not search or search.lower() in p["name"].lower()
                     or search.lower() in p["role"].lower())]

    if filtered:
        s_cols = st.columns(3)
        for i, person in enumerate(filtered):
            with s_cols[i % 3]:
                st.markdown(f"""
                <div style='background:white; padding:1rem; border-radius:12px;
                            box-shadow:0 2px 6px rgba(0,0,0,0.07); text-align:center;
                            margin-bottom:0.8rem;'>
                    <div style='font-size:2.5rem;'>{person["avatar"]}</div>
                    <div style='font-weight:600; color:#0d1b2a;'>{person["name"]}</div>
                    <div style='color:#555; font-size:0.8rem;'>{person["role"]}</div>
                    <div style='color:#999; font-size:0.75rem;'>{person["mutual"]} mutual connections</div>
                </div>""", unsafe_allow_html=True)
                if st.button("➕ Connect", key=f"conn_{i}"):
                    st.session_state.connections.append(person["name"])
                    st.success(f"Connected with {person['name']}!")
                    st.rerun()
    else:
        st.info("No new suggestions right now.")
