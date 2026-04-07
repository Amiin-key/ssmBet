import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

# --- 1. CONFIG (STYLING) ---
st.set_page_config(page_title="SSM Pro Investment", page_icon="📈", layout="wide")

# --- 2. SESSION STATE (USER DATA) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = "Guest"

# --- 3. API FUNCTION ---
def get_btc():
    try:
        url = "https://coingecko.com"
        res = requests.get(url).json()
        return res['bitcoin']['usd']
    except:
        return 65000.0

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("SSM PRO")
    lang = st.radio("Luuqadda", ["Somali", "English"])
    if st.session_state.logged_in:
        st.write("---")
        st.write(f"👤 Account: **{st.session_state.user}**")
        st.write("✅ Verified Status")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()

# --- 5. LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("Welcome to SSM Investment")
    col1, col2 = st.columns(2)
    with col1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login / Sign Up"):
            if u and p:
                st.session_state.logged_in = True
                st.session_state.user = u
                st.rerun()

# --- 6. DASHBOARD PAGE ---
else:
    btc_p = get_btc()
    
    # Layout Dashboard
    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        # Portfolio Card
        st.subheader("Hantidaada / Your Portfolio")
        st.info(f"TOTAL BALANCE: $2,450.75")
        
        # Live Chart
        fig = go.Figure(go.Scatter(y=[64000, 65500, 65200, 66800, btc_p], 
                                 line=dict(color='#00FF7F', width=4),
                                 mode='lines+markers'))
        fig.update_layout(title="BTC Market Trend", 
                         paper_bgcolor='black', 
                         plot_bgcolor='black', 
                         font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)

    with col_side:
        st.subheader("Market Live")
        st.metric("Bitcoin (BTC)", f"${btc_p:,.2f}", "+1.5%")
        
        st.write("---")
        st.subheader("💰 Deposit")
        st.warning("EVC Plus: 061XXXXXXX")
        with st.expander("Sida loo shubto (Steps)"):
            st.write("1. Garaac *712#")
            st.write("2. U dir lacagta nambarka kore")
            st.write("3. TXID-ga u dir WhatsApp-ka")
        
        # WhatsApp Link
        st.link_button("💬 WhatsApp Support", "https://wa.me")

    # Bottom Table
    st.write("---")
    st.subheader("Assets Details")
    data = {
        "Asset": ["Bitcoin (BTC)", "Cash (USD)"],
        "Amount": ["0.015 BTC", "$1,450.75"],
        "Current Value": [f"${0.015*btc_p:,.2f}", "$1,450.75"]
    }
    st.table(pd.DataFrame(data))
