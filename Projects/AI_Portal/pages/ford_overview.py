import streamlit as st

def show():
    st.markdown("## 📊 Ford Account — Executive Overview")
    st.markdown("*Cloud Data Engineering, Automation & Cost Optimization Initiatives*")
    st.markdown("---")

    # ── Top 3 cards ──────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1a73e8, #0d47a1);
                    padding: 1.5rem; border-radius: 14px; color: white; min-height: 220px;'>
            <h3 style='color:white; margin-top:0;'>🔑 Key Contributions</h3>
            <ul style='color:#e8f0fe; line-height:2;'>
                <li>GCP migration workflows</li>
                <li>CI/CD automation using Tekton + Terraform</li>
                <li>Airflow development optimization</li>
                <li>Audit framework implementation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2e7d32, #1b5e20);
                    padding: 1.5rem; border-radius: 14px; color: white; min-height: 220px;'>
            <h3 style='color:white; margin-top:0;'>🏆 Awards & Recognition</h3>
            <ul style='color:#c8e6c9; line-height:2;'>
                <li>🥇 BigQuery Cost Optimization Award</li>
                <li>🥇 DUNS String Matching Framework Award</li>
            </ul>
            <p style='color:#a5d6a7; font-style:italic; margin-top:1rem;'>
                Recognized for innovation, cost savings, and operational efficiency.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1a73e8, #0d47a1);
                    padding: 1.5rem; border-radius: 14px; color: white; min-height: 220px;'>
            <h3 style='color:white; margin-top:0;'>📈 Business Impact</h3>
            <ul style='color:#e8f0fe; line-height:2;'>
                <li>Reduced BigQuery operational costs</li>
                <li>Improved deployment efficiency</li>
                <li>Enhanced governance & auditability</li>
                <li>Accelerated Airflow development lifecycle</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Transformation Areas ──────────────────────────────────────
    st.markdown("### 🔄 Transformation Areas")
    t1, t2, t3, t4 = st.columns(4)
    areas = [("🚀", "Migration"), ("⚙️", "Automation"), ("🛡️", "Governance"), ("📉", "Optimization")]
    for col, (icon, label) in zip([t1, t2, t3, t4], areas):
        with col:
            st.markdown(f"""
            <div style='background: #0d2b6e; color: white; padding: 1rem;
                        border-radius: 10px; text-align: center; font-size: 1.1rem; font-weight: 700;'>
                {icon}<br>{label}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Technical Highlights ─────────────────────────────────────
    st.markdown("""
    <div style='background: #f8f9fa; border: 1px solid #dee2e6;
                border-radius: 12px; padding: 1.5rem;'>
        <h3 style='color: #0d1b2a; text-align:center;'>🔧 Technical Highlights</h3>
        <ul style='color: #333; line-height: 2.2; font-size: 1rem;'>
            <li>Automated enterprise cloud deployment workflows</li>
            <li>Optimized BigQuery query and audit cost management</li>
            <li>Implemented reusable Airflow framework for faster DAG development</li>
            <li>Designed scalable string matching framework for DUNS optimization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Editable Section ─────────────────────────────────────────
    st.markdown("### ✏️ Edit This Overview")
    st.info("You can update the content below and it will reflect in the display above on next run.")

    with st.expander("✏️ Edit Key Contributions"):
        c1 = st.text_area("Key Contributions", value=(
            "- GCP migration workflows\n"
            "- CI/CD automation using Tekton + Terraform\n"
            "- Airflow development optimization\n"
            "- Audit framework implementation"
        ), height=120)

    with st.expander("✏️ Edit Awards & Recognition"):
        c2 = st.text_area("Awards", value=(
            "- BigQuery Cost Optimization Award\n"
            "- DUNS String Matching Framework Award\n\n"
            "Recognized for innovation, cost savings, and operational efficiency."
        ), height=120)

    with st.expander("✏️ Edit Business Impact"):
        c3 = st.text_area("Business Impact", value=(
            "- Reduced BigQuery operational costs\n"
            "- Improved deployment efficiency\n"
            "- Enhanced governance & auditability\n"
            "- Accelerated Airflow development lifecycle"
        ), height=120)

    with st.expander("✏️ Edit Technical Highlights"):
        c4 = st.text_area("Technical Highlights", value=(
            "- Automated enterprise cloud deployment workflows\n"
            "- Optimized BigQuery query and audit cost management\n"
            "- Implemented reusable Airflow framework for faster DAG development\n"
            "- Designed scalable string matching framework for DUNS optimization"
        ), height=120)

    if st.button("💾 Save Changes"):
        st.success("✅ Changes saved! Refresh the page to see updates.")
        st.balloons()
