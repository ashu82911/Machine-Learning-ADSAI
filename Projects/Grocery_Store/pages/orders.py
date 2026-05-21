import streamlit as st

STATUS_COLOR = {
    "Confirmed ✅": "#2e7d32",
    "Out for Delivery 🚚": "#f57c00",
    "Delivered 🎉": "#1565c0",
    "Cancelled ❌": "#e53935",
}

def show():
    st.markdown("## 📦 My Orders")

    if not st.session_state.orders:
        st.markdown("""
        <div style='text-align:center;padding:4rem;background:white;border-radius:20px;
                    box-shadow:0 4px 12px rgba(0,0,0,0.08);'>
            <div style='font-size:5rem;'>📦</div>
            <h3 style='color:#555;'>No orders yet!</h3>
            <p style='color:#999;'>Place your first order from the cart.</p>
        </div>""", unsafe_allow_html=True)
        return

    for order in reversed(st.session_state.orders):
        color = STATUS_COLOR.get(order["status"], "#555")
        items_html = ""
        for pid, qty in order["items"].items():
            p = next((x for x in st.session_state.products if x["id"]==pid), None)
            if p:
                items_html += f"<span style='background:#e8f5e9;color:#2e7d32;padding:3px 10px;border-radius:12px;font-size:0.78rem;margin:2px;display:inline-block;'>🛒 {p['name']} x{qty}</span>"

        st.markdown(f"""
        <div style='background:white;border-radius:16px;padding:1.5rem;
                    margin-bottom:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.08);
                    border-left:5px solid {color};'>
            <div style='display:flex;justify-content:space-between;align-items:center;'>
                <div>
                    <span style='font-weight:800;color:#1b5e20;font-size:1rem;'>#{order["id"]}</span>
                    <span style='color:#999;font-size:0.8rem;margin-left:1rem;'>🕐 {order["time"]}</span>
                </div>
                <span style='background:{color}22;color:{color};padding:4px 14px;
                             border-radius:20px;font-size:0.82rem;font-weight:700;'>
                    {order["status"]}</span>
            </div>
            <div style='margin:0.8rem 0;'>{items_html}</div>
            <div style='display:flex;gap:2rem;flex-wrap:wrap;margin-top:0.5rem;'>
                <div style='color:#555;font-size:0.85rem;'>👤 {order["name"]}</div>
                <div style='color:#555;font-size:0.85rem;'>📞 {order["phone"]}</div>
                <div style='color:#555;font-size:0.85rem;'>💳 {order["payment"]}</div>
                <div style='color:#1b5e20;font-weight:800;font-size:1rem;'>💰 ₹{order["total"]}</div>
            </div>
            <div style='color:#777;font-size:0.82rem;margin-top:4px;'>📍 {order["address"]}</div>
        </div>""", unsafe_allow_html=True)

        # Update status
        col1, col2 = st.columns([2,3])
        with col1:
            new_status = st.selectbox("Update Status", list(STATUS_COLOR.keys()),
                                      key=f"status_{order['id']}",
                                      index=list(STATUS_COLOR.keys()).index(order["status"]))
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("💾 Update", key=f"upd_{order['id']}"):
                order["status"] = new_status
                st.success("Status updated!")
                st.rerun()
