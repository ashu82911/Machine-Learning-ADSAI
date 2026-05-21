import streamlit as st
from datetime import datetime
import random

def show():
    st.markdown("## 🛒 My Cart")

    if not st.session_state.cart:
        st.markdown("""
        <div style='text-align:center;padding:4rem;background:white;border-radius:20px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08);'>
            <div style='font-size:5rem;'>🛒</div>
            <h3 style='color:#555;'>Your cart is empty!</h3>
            <p style='color:#999;'>Go to Products and add items to your cart.</p>
        </div>""", unsafe_allow_html=True)
        return

    col_cart, col_summary = st.columns([3, 1])

    with col_cart:
        st.markdown("### 🧺 Cart Items")
        subtotal = 0

        for pid, qty in list(st.session_state.cart.items()):
            p = next((x for x in st.session_state.products if x["id"] == pid), None)
            if not p: continue
            item_total = p["price"] * qty
            subtotal += item_total

            st.markdown(f"""
            <div style='background:white;border-radius:14px;padding:1rem 1.2rem;
                        margin-bottom:0.8rem;box-shadow:0 4px 12px rgba(0,0,0,0.07);
                        display:flex;align-items:center;gap:1rem;'>
                <img src='{p["image"]}' style='width:80px;height:80px;
                     object-fit:cover;border-radius:10px;flex-shrink:0;'/>
                <div style='flex:1;'>
                    <div style='font-weight:700;color:#1b5e20;font-size:0.95rem;'>{p["name"]}</div>
                    <div style='color:#555;font-size:0.82rem;'>₹{p["price"]} per {p["unit"]}</div>
                    <div style='color:#2e7d32;font-weight:800;font-size:1rem;'>₹{item_total}</div>
                </div>
            </div>""", unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns([1,1,1,2])
            with c1:
                if st.button("➖", key=f"cart_dec_{pid}"):
                    if st.session_state.cart[pid] > 1:
                        st.session_state.cart[pid] -= 1
                    else:
                        del st.session_state.cart[pid]
                    st.rerun()
            with c2:
                st.markdown(f"""
                <div style='text-align:center;background:#e8f5e9;border-radius:8px;
                            padding:8px;font-weight:700;color:#2e7d32;font-size:1rem;'>{qty}</div>
                """, unsafe_allow_html=True)
            with c3:
                if st.button("➕", key=f"cart_inc_{pid}"):
                    st.session_state.cart[pid] += 1
                    st.rerun()
            with c4:
                if st.button("🗑️ Remove", key=f"cart_rem_{pid}"):
                    del st.session_state.cart[pid]
                    st.rerun()

        if st.button("🗑️ Clear Entire Cart"):
            st.session_state.cart = {}
            st.rerun()

    with col_summary:
        subtotal = sum(
            next((p["price"] for p in st.session_state.products if p["id"]==pid),0)*qty
            for pid,qty in st.session_state.cart.items()
        )
        delivery = 0 if subtotal >= 500 else 40
        discount = round(subtotal * 0.05) if subtotal >= 300 else 0
        total = subtotal + delivery - discount

        st.markdown(f"""
        <div style='background:white;border-radius:16px;padding:1.5rem;
                    box-shadow:0 4px 16px rgba(0,0,0,0.1);position:sticky;top:1rem;'>
            <h3 style='color:#1b5e20;margin-top:0;'>🧾 Bill Summary</h3>
            <div style='border-top:1px solid #e8f5e9;padding-top:1rem;'>
                <div style='display:flex;justify-content:space-between;margin:8px 0;color:#555;'>
                    <span>Subtotal</span><span>₹{subtotal}</span>
                </div>
                <div style='display:flex;justify-content:space-between;margin:8px 0;color:#555;'>
                    <span>Delivery</span>
                    <span style='color:{"#2e7d32" if delivery==0 else "#555"};'>
                        {"🆓 FREE" if delivery==0 else f"₹{delivery}"}</span>
                </div>
                {'<div style="display:flex;justify-content:space-between;margin:8px 0;color:#e53935;"><span>Discount (5%)</span><span>-₹'+str(discount)+'</span></div>' if discount else ''}
                <div style='border-top:2px solid #e8f5e9;margin-top:1rem;padding-top:1rem;
                            display:flex;justify-content:space-between;font-weight:800;
                            font-size:1.2rem;color:#1b5e20;'>
                    <span>Total</span><span>₹{total}</span>
                </div>
                {'<div style="color:#2e7d32;font-size:0.78rem;margin-top:4px;">✅ You saved ₹'+str(discount)+'!</div>' if discount else ''}
                {'<div style="color:#f57c00;font-size:0.78rem;margin-top:4px;">Add ₹'+str(500-subtotal)+' more for FREE delivery!</div>' if subtotal < 500 else '<div style="color:#2e7d32;font-size:0.78rem;margin-top:4px;">🚚 FREE delivery applied!</div>'}
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Checkout form
        st.markdown("### 📍 Delivery Details")
        name    = st.text_input("Full Name",    placeholder="Ashutosh Kumar Pandey")
        phone   = st.text_input("Phone",        placeholder="9876543210")
        address = st.text_area("Address",       placeholder="House No, Street, City, PIN", height=80)
        payment = st.selectbox("💳 Payment",    ["Cash on Delivery","UPI","Net Banking","Card"])

        if st.button("✅ Place Order", type="primary"):
            if name and phone and address:
                order_id = f"ORD{random.randint(10000,99999)}"
                order = {
                    "id": order_id,
                    "items": dict(st.session_state.cart),
                    "total": total,
                    "name": name,
                    "phone": phone,
                    "address": address,
                    "payment": payment,
                    "status": "Confirmed ✅",
                    "time": datetime.now().strftime("%d %b %Y, %I:%M %p")
                }
                st.session_state.orders.append(order)
                st.session_state.cart = {}
                st.success(f"🎉 Order placed! ID: **{order_id}**")
                st.balloons()
                st.rerun()
            else:
                st.error("Please fill all delivery details!")
