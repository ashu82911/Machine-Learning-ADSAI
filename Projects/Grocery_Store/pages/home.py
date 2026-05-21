import streamlit as st

def show():
    # Hero
    st.markdown("""
    <div style='background:linear-gradient(135deg,#1b5e20,#2e7d32,#43a047);
                padding:3rem 2rem; border-radius:20px; text-align:center;
                margin-bottom:2rem; position:relative; overflow:hidden;'>
        <img src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=1200&q=60'
             style='position:absolute;top:0;left:0;width:100%;height:100%;
                    object-fit:cover;opacity:0.2;border-radius:20px;'/>
        <div style='position:relative;'>
            <div style='font-size:3.5rem;'>🛒</div>
            <h1 style='color:white;font-size:2.8rem;margin:0.3rem 0;font-weight:800;'>
                Ashu General Store</h1>
            <p style='color:#c8e6c9;font-size:1.1rem;margin:0;'>
                Fresh Groceries · Daily Essentials · Best Prices in Town</p>
            <div style='margin-top:1.2rem;'>
                <span style='background:rgba(255,255,255,0.2);color:white;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;'>
                    🥦 Fresh Vegetables</span>
                <span style='background:rgba(255,255,255,0.2);color:white;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;'>
                    🥛 Dairy Products</span>
                <span style='background:rgba(255,255,255,0.2);color:white;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;'>
                    🌾 Grains & Pulses</span>
                <span style='background:rgba(255,255,255,0.2);color:white;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;'>
                    🚚 Free Delivery ₹500+</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # Stats
    s1,s2,s3,s4 = st.columns(4)
    cart_count = sum(st.session_state.cart.values())
    total = sum(next((p["price"] for p in st.session_state.products if p["id"]==pid),0)*qty
                for pid,qty in st.session_state.cart.items())
    for col,(icon,val,label,color) in zip([s1,s2,s3,s4],[
        ("🛍️", len(st.session_state.products), "Products",   "#2e7d32"),
        ("🛒", cart_count,                      "In Cart",    "#f57c00"),
        ("💰", f"₹{total}",                     "Cart Value", "#1565c0"),
        ("📦", len(st.session_state.orders),    "Orders",     "#9c27b0"),
    ]):
        with col:
            st.markdown(f"""
            <div style='background:white;padding:1.2rem;border-radius:14px;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08);text-align:center;
                        border-bottom:3px solid {color};'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:1.8rem;font-weight:800;color:{color};'>{val}</div>
                <div style='color:#777;font-size:0.82rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Categories
    st.markdown("### 🗂️ Shop by Category")
    cats = [
        ("🥦","Vegetables","#2e7d32","https://images.unsplash.com/photo-1540420773420-3366772f4999?w=300&q=70"),
        ("🍎","Fruits",    "#e53935","https://images.unsplash.com/photo-1619566636858-adf3ef46400b?w=300&q=70"),
        ("🥛","Dairy",     "#1565c0","https://images.unsplash.com/photo-1550583724-b2692b85b150?w=300&q=70"),
        ("🌾","Grains",    "#f57c00","https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300&q=70"),
        ("🍟","Snacks",    "#9c27b0","https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=300&q=70"),
        ("☕","Beverages", "#00897b","https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=300&q=70"),
    ]
    c_cols = st.columns(6)
    for col,(icon,name,color,img) in zip(c_cols,cats):
        with col:
            st.markdown(f"""
            <div style='background:white;border-radius:14px;overflow:hidden;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08);text-align:center;
                        cursor:pointer;'>
                <img src='{img}' style='width:100%;height:90px;object-fit:cover;'/>
                <div style='padding:0.6rem;border-top:3px solid {color};'>
                    <div style='font-size:1.3rem;'>{icon}</div>
                    <div style='font-weight:600;color:{color};font-size:0.82rem;'>{name}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Featured products
    st.markdown("### ⭐ Featured Products")
    featured = st.session_state.products[:6]
    f_cols = st.columns(3)
    for i, p in enumerate(featured):
        with f_cols[i % 3]:
            st.markdown(f"""
            <div style='background:white;border-radius:14px;overflow:hidden;
                        box-shadow:0 4px 12px rgba(0,0,0,0.08);margin-bottom:1rem;'>
                <img src='{p["image"]}' style='width:100%;height:160px;object-fit:cover;'/>
                <div style='padding:0.8rem 1rem;'>
                    <div style='font-weight:700;color:#1b5e20;font-size:0.95rem;'>{p["name"]}</div>
                    <div style='color:#2e7d32;font-size:1.1rem;font-weight:800;'>₹{p["price"]}
                        <span style='color:#999;font-size:0.75rem;font-weight:400;'>/{p["unit"]}</span>
                    </div>
                    <div style='color:#999;font-size:0.75rem;'>Stock: {p["stock"]} {p["unit"]}</div>
                </div>
            </div>""", unsafe_allow_html=True)
            if st.button(f"🛒 Add to Cart", key=f"home_add_{p['id']}"):
                st.session_state.cart[p["id"]] = st.session_state.cart.get(p["id"], 0) + 1
                st.success(f"✅ {p['name']} added!")
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:linear-gradient(90deg,#e8f5e9,#f1f8e9);padding:1.2rem 2rem;
                border-radius:14px;border-left:5px solid #2e7d32;'>
        <h4 style='color:#1b5e20;margin:0;'>🚚 Free Delivery on orders above ₹500!</h4>
        <p style='color:#555;margin:4px 0 0 0;font-size:0.9rem;'>
            Same day delivery available · Fresh produce guaranteed · Easy returns</p>
    </div>""", unsafe_allow_html=True)
