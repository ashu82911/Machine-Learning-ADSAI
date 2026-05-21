import streamlit as st

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0d1b2a 0%, #1a73e8 100%);
                padding: 3rem; border-radius: 16px; text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: white; font-size: 3rem; margin: 0;'>🤖 AshTech AI Portal</h1>
        <p style='color: #cce0ff; font-size: 1.2rem; margin-top: 1rem;'>
            Your gateway to AI-powered Job Search & Technical Knowledge
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style='background:white; padding:1.5rem; border-radius:12px;
                    box-shadow:0 2px 12px rgba(0,0,0,0.08); text-align:center;'>
            <div style='font-size:2.5rem;'>💼</div>
            <h3 style='color:#1a73e8;'>Job Search</h3>
            <p style='color:#555;'>Browse AI/ML, Data Science & Tech jobs curated for you</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:white; padding:1.5rem; border-radius:12px;
                    box-shadow:0 2px 12px rgba(0,0,0,0.08); text-align:center;'>
            <div style='font-size:2.5rem;'>🤖</div>
            <h3 style='color:#1a73e8;'>AI Chatbot</h3>
            <p style='color:#555;'>Ask anything about AI, ML, Data Science & career guidance</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='background:white; padding:1.5rem; border-radius:12px;
                    box-shadow:0 2px 12px rgba(0,0,0,0.08); text-align:center;'>
            <div style='font-size:2.5rem;'>📚</div>
            <h3 style='color:#1a73e8;'>Knowledge Base</h3>
            <p style='color:#555;'>Learn ML, Deep Learning, NLP, Cloud & more</p>
        </div>""", unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style='background:white; padding:1.5rem; border-radius:12px;
                    box-shadow:0 2px 12px rgba(0,0,0,0.08); text-align:center;'>
            <div style='font-size:2.5rem;'>📊</div>
            <h3 style='color:#1a73e8;'>Ford Overview</h3>
            <p style='color:#555;'>Cloud Data Engineering & Cost Optimization insights</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Why AshTech AI Portal?")
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("✅ AI-powered job recommendations")
        st.success("✅ Real-time technical Q&A chatbot")
        st.success("✅ Structured ML/AI learning paths")
    with col_b:
        st.info("🎯 Built for AI/ML professionals")
        st.info("🎯 Interview prep & career guidance")
        st.info("🎯 Industry project showcases")
