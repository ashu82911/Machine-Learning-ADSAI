import streamlit as st
from pages import home, products, cart, orders, admin

st.set_page_config(
    page_title="Ashu General Store",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 60%, #388e3c 100%) !important;
}
[data-testid="stSidebar"] * { color: #f1f8e9 !important; }
.main { background: #f9fbe7; }
.stButton>button {
    background: linear-gradient(90deg, #2e7d32, #1b5e20);
    color: white !important; border-radius: 10px; border: none;
    padding: 0.5rem 1.5rem; font-weight: 600;
    box-shadow: 0 2px 8px rgba(46,125,50,0.3); transition: all 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1b5e20, #0a3d0a);
    box-shadow: 0 4px 16px rgba(46,125,50,0.5); transform: translateY(-1px);
}
.stTextInput>div>div>input { border-radius: 10px; border: 1.5px solid #c8e6c9; }
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = {}          # {product_id: qty}
if "orders" not in st.session_state:
    st.session_state.orders = []
if "products" not in st.session_state:
    st.session_state.products = [
        # Fruits & Vegetables
        {"id":1,  "name":"Fresh Tomatoes",    "category":"Vegetables", "price":30,  "unit":"kg",  "stock":50, "image":"https://images.unsplash.com/photo-1546094096-0df4bcaaa337?w=300&q=70"},
        {"id":2,  "name":"Onions",            "category":"Vegetables", "price":25,  "unit":"kg",  "stock":80, "image":"https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=300&q=70"},
        {"id":3,  "name":"Potatoes",          "category":"Vegetables", "price":20,  "unit":"kg",  "stock":100,"image":"https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=300&q=70"},
        {"id":4,  "name":"Bananas",           "category":"Fruits",     "price":40,  "unit":"doz", "stock":30, "image":"https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=300&q=70"},
        {"id":5,  "name":"Apples",            "category":"Fruits",     "price":120, "unit":"kg",  "stock":25, "image":"https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300&q=70"},
        {"id":6,  "name":"Spinach",           "category":"Vegetables", "price":15,  "unit":"bunch","stock":40,"image":"https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=300&q=70"},
        # Dairy
        {"id":7,  "name":"Amul Milk 1L",      "category":"Dairy",      "price":58,  "unit":"pkt", "stock":60, "image":"https://images.unsplash.com/photo-1550583724-b2692b85b150?w=300&q=70"},
        {"id":8,  "name":"Paneer 200g",       "category":"Dairy",      "price":80,  "unit":"pkt", "stock":20, "image":"https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=300&q=70"},
        {"id":9,  "name":"Curd 400g",         "category":"Dairy",      "price":45,  "unit":"pkt", "stock":35, "image":"https://images.unsplash.com/photo-1488477181946-6428a0291777?w=300&q=70"},
        # Grains
        {"id":10, "name":"Basmati Rice 5kg",  "category":"Grains",     "price":350, "unit":"bag", "stock":15, "image":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300&q=70"},
        {"id":11, "name":"Wheat Flour 5kg",   "category":"Grains",     "price":220, "unit":"bag", "stock":20, "image":"https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=300&q=70"},
        {"id":12, "name":"Toor Dal 1kg",      "category":"Grains",     "price":130, "unit":"kg",  "stock":40, "image":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=300&q=70"},
        # Snacks
        {"id":13, "name":"Lay's Chips",       "category":"Snacks",     "price":20,  "unit":"pkt", "stock":50, "image":"https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=300&q=70"},
        {"id":14, "name":"Biscuits Parle-G",  "category":"Snacks",     "price":10,  "unit":"pkt", "stock":100,"image":"https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=300&q=70"},
        # Beverages
        {"id":15, "name":"Tata Tea 250g",     "category":"Beverages",  "price":85,  "unit":"pkt", "stock":30, "image":"https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=300&q=70"},
        {"id":16, "name":"Nescafe Coffee",    "category":"Beverages",  "price":220, "unit":"jar", "stock":15, "image":"https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=300&q=70"},
        # Oils & Spices
        {"id":17, "name":"Sunflower Oil 1L",  "category":"Oils",       "price":140, "unit":"btl", "stock":25, "image":"https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300&q=70"},
        {"id":18, "name":"Turmeric Powder",   "category":"Spices",     "price":45,  "unit":"pkt", "stock":60, "image":"https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=300&q=70"},
    ]

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:1rem 0;'>
        <div style='font-size:3rem;'>🛒</div>
        <h2 style='color:#f1f8e9 !important; margin:0; font-size:1.4rem;'>Ashu General Store</h2>
        <p style='color:#c8e6c9 !important; font-size:0.8rem; margin:0;'>Fresh · Fast · Affordable</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    cart_count = sum(st.session_state.cart.values())
    cart_label = f"🛒  My Cart  ({cart_count})" if cart_count else "🛒  My Cart"

    page = st.radio("", [
        "🏠  Home",
        "🛍️  Products",
        cart_label,
        "📦  My Orders",
        "⚙️  Admin Panel",
    ])
    st.markdown("---")

    # Cart total in sidebar
    if cart_count:
        total = sum(
            next((p["price"] for p in st.session_state.products if p["id"] == pid), 0) * qty
            for pid, qty in st.session_state.cart.items()
        )
        st.markdown(f"""
        <div style='background:rgba(255,255,255,0.15); border-radius:10px; padding:0.8rem; text-align:center;'>
            <div style='color:#f1f8e9 !important; font-size:0.85rem;'>Cart Total</div>
            <div style='color:#a5d6a7 !important; font-size:1.5rem; font-weight:800;'>₹{total}</div>
            <div style='color:#c8e6c9 !important; font-size:0.75rem;'>{cart_count} items</div>
        </div>""", unsafe_allow_html=True)

# ── Route ────────────────────────────────────────────────────
if   "Home"    in page: home.show()
elif "Product" in page: products.show()
elif "Cart"    in page: cart.show()
elif "Orders"  in page: orders.show()
elif "Admin"   in page: admin.show()
