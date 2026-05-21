import streamlit as st

def show():
    st.markdown("## ⚙️ Admin Panel")

    # Password
    if "admin_auth" not in st.session_state:
        st.session_state.admin_auth = False

    if not st.session_state.admin_auth:
        st.markdown("""
        <div style='max-width:400px;margin:3rem auto;background:white;padding:2rem;
                    border-radius:16px;box-shadow:0 4px 16px rgba(0,0,0,0.1);text-align:center;'>
            <div style='font-size:3rem;'>🔐</div>
            <h3 style='color:#1b5e20;'>Admin Login</h3>
        </div>""", unsafe_allow_html=True)
        pwd = st.text_input("Password", type="password", placeholder="Enter admin password")
        if st.button("🔓 Login"):
            if pwd == "ashu123":
                st.session_state.admin_auth = True
                st.rerun()
            else:
                st.error("Wrong password! (Hint: ashu123)")
        return

    tab1, tab2, tab3 = st.tabs(["📦 Manage Products", "📊 Sales Dashboard", "➕ Add Product"])

    with tab1:
        st.markdown("### 📦 Product Inventory")
        for p in st.session_state.products:
            stock_color = "#2e7d32" if p["stock"]>10 else "#f57c00" if p["stock"]>0 else "#e53935"
            c1,c2,c3,c4,c5 = st.columns([3,1,1,1,1])
            with c1:
                st.markdown(f"""
                <div style='display:flex;align-items:center;gap:10px;'>
                    <img src='{p["image"]}' width='45' style='border-radius:8px;object-fit:cover;height:45px;'/>
                    <div>
                        <div style='font-weight:600;color:#1b5e20;font-size:0.88rem;'>{p["name"]}</div>
                        <div style='color:#999;font-size:0.75rem;'>{p["category"]}</div>
                    </div>
                </div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div style='color:#2e7d32;font-weight:700;padding-top:12px;'>₹{p['price']}</div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div style='color:{stock_color};font-weight:600;padding-top:12px;'>{p['stock']}</div>", unsafe_allow_html=True)
            with c4:
                new_stock = st.number_input("", min_value=0, value=p["stock"],
                                            key=f"stk_{p['id']}", label_visibility="collapsed")
            with c5:
                if st.button("💾", key=f"save_{p['id']}"):
                    p["stock"] = new_stock
                    st.success("Updated!")
                    st.rerun()

    with tab2:
        st.markdown("### 📊 Sales Dashboard")
        total_orders  = len(st.session_state.orders)
        total_revenue = sum(o["total"] for o in st.session_state.orders)
        total_items   = sum(sum(v for v in o["items"].values()) for o in st.session_state.orders)

        m1,m2,m3 = st.columns(3)
        for col,(icon,val,label,color) in zip([m1,m2,m3],[
            ("📦", total_orders,   "Total Orders",   "#2e7d32"),
            ("💰", f"₹{total_revenue}", "Revenue",   "#1565c0"),
            ("🛒", total_items,    "Items Sold",     "#f57c00"),
        ]):
            with col:
                st.markdown(f"""
                <div style='background:white;padding:1.5rem;border-radius:14px;
                            box-shadow:0 4px 12px rgba(0,0,0,0.08);text-align:center;
                            border-bottom:3px solid {color};'>
                    <div style='font-size:2rem;'>{icon}</div>
                    <div style='font-size:2rem;font-weight:800;color:{color};'>{val}</div>
                    <div style='color:#777;'>{label}</div>
                </div>""", unsafe_allow_html=True)

        if st.session_state.orders:
            st.markdown("<br>### 📋 Recent Orders")
            for o in reversed(st.session_state.orders[-5:]):
                st.markdown(f"""
                <div style='background:#f8f9fa;border-radius:10px;padding:0.8rem 1rem;
                            margin:4px 0;display:flex;justify-content:space-between;'>
                    <span style='font-weight:600;color:#1b5e20;'>#{o["id"]}</span>
                    <span style='color:#555;'>{o["name"]}</span>
                    <span style='color:#2e7d32;font-weight:700;'>₹{o["total"]}</span>
                    <span style='color:#f57c00;'>{o["status"]}</span>
                </div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown("### ➕ Add New Product")
        c1,c2 = st.columns(2)
        with c1:
            new_name  = st.text_input("Product Name")
            new_price = st.number_input("Price (₹)", min_value=1, value=50)
            new_stock = st.number_input("Stock", min_value=0, value=10)
        with c2:
            new_cat   = st.selectbox("Category", ["Vegetables","Fruits","Dairy","Grains","Snacks","Beverages","Oils","Spices"])
            new_unit  = st.selectbox("Unit", ["kg","pkt","btl","jar","doz","bunch","bag"])
            new_img   = st.text_input("Image URL", placeholder="https://images.unsplash.com/...")

        if st.button("➕ Add Product", type="primary"):
            if new_name:
                new_id = max(p["id"] for p in st.session_state.products) + 1
                st.session_state.products.append({
                    "id": new_id, "name": new_name, "category": new_cat,
                    "price": new_price, "unit": new_unit, "stock": new_stock,
                    "image": new_img or "https://images.unsplash.com/photo-1542838132-92c53300491e?w=300&q=70"
                })
                st.success(f"✅ '{new_name}' added successfully!")
                st.rerun()
            else:
                st.error("Product name is required!")

    if st.button("🔒 Logout"):
        st.session_state.admin_auth = False
        st.rerun()
