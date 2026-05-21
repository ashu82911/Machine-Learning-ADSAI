import streamlit as st

def show():
    st.markdown("## 🛍️ All Products")

    # Filters
    col1, col2, col3 = st.columns([3,2,2])
    with col1:
        search = st.text_input("🔍 Search products", placeholder="e.g. tomato, milk, rice...")
    with col2:
        cats = ["All"] + sorted(set(p["category"] for p in st.session_state.products))
        cat = st.selectbox("📂 Category", cats)
    with col3:
        sort = st.selectbox("↕️ Sort by", ["Default","Price: Low to High","Price: High to Low","Name A-Z"])

    st.markdown("---")

    # Filter
    prods = st.session_state.products
    if search:
        prods = [p for p in prods if search.lower() in p["name"].lower()]
    if cat != "All":
        prods = [p for p in prods if p["category"] == cat]
    if sort == "Price: Low to High":
        prods = sorted(prods, key=lambda x: x["price"])
    elif sort == "Price: High to Low":
        prods = sorted(prods, key=lambda x: x["price"], reverse=True)
    elif sort == "Name A-Z":
        prods = sorted(prods, key=lambda x: x["name"])

    st.markdown(f"**{len(prods)} products found**")

    # Grid
    cols = st.columns(4)
    for i, p in enumerate(prods):
        with cols[i % 4]:
            in_cart = st.session_state.cart.get(p["id"], 0)
            stock_color = "#2e7d32" if p["stock"] > 10 else "#f57c00" if p["stock"] > 0 else "#e53935"
            stock_label = f"✅ {p['stock']} left" if p["stock"] > 10 else f"⚠️ Only {p['stock']} left" if p["stock"] > 0 else "❌ Out of Stock"

            st.markdown(f"""
            <div style='background:white;border-radius:14px;overflow:hidden;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08);margin-bottom:1rem;'>
                <div style='position:relative;'>
                    <img src='{p["image"]}' style='width:100%;height:150px;object-fit:cover;'/>
                    <span style='position:absolute;top:8px;right:8px;background:#2e7d32;
                                 color:white;padding:2px 8px;border-radius:12px;font-size:0.7rem;
                                 font-weight:600;'>{p["category"]}</span>
                    {f'<span style="position:absolute;top:8px;left:8px;background:#f57c00;color:white;padding:2px 8px;border-radius:12px;font-size:0.7rem;font-weight:600;">In Cart: {in_cart}</span>' if in_cart else ''}
                </div>
                <div style='padding:0.8rem;'>
                    <div style='font-weight:700;color:#1b5e20;font-size:0.9rem;
                                white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>
                        {p["name"]}</div>
                    <div style='color:#2e7d32;font-size:1.1rem;font-weight:800;margin:4px 0;'>
                        ₹{p["price"]}
                        <span style='color:#999;font-size:0.72rem;font-weight:400;'>/{p["unit"]}</span>
                    </div>
                    <div style='color:{stock_color};font-size:0.72rem;font-weight:600;'>{stock_label}</div>
                </div>
            </div>""", unsafe_allow_html=True)

            if p["stock"] > 0:
                c1, c2, c3 = st.columns([1,2,1])
                with c1:
                    if st.button("➖", key=f"dec_{p['id']}"):
                        if st.session_state.cart.get(p["id"], 0) > 0:
                            st.session_state.cart[p["id"]] -= 1
                            if st.session_state.cart[p["id"]] == 0:
                                del st.session_state.cart[p["id"]]
                            st.rerun()
                with c2:
                    qty = st.session_state.cart.get(p["id"], 0)
                    st.markdown(f"""
                    <div style='text-align:center;background:#e8f5e9;border-radius:8px;
                                padding:6px;font-weight:700;color:#2e7d32;'>{qty}</div>
                    """, unsafe_allow_html=True)
                with c3:
                    if st.button("➕", key=f"inc_{p['id']}"):
                        st.session_state.cart[p["id"]] = st.session_state.cart.get(p["id"], 0) + 1
                        st.rerun()
            else:
                st.button("❌ Out of Stock", key=f"oos_{p['id']}", disabled=True)
