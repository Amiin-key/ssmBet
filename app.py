import streamlit as st
from datetime import datetime
import random

# ===== SETTINGS =====
st.set_page_config(page_title="SSM PRO", page_icon="💰", layout="wide")

# --- Luuqad toggle ---
if "isSomali" not in st.session_state:
    st.session_state.isSomali = True

def toggle_lang():
    st.session_state.isSomali = not st.session_state.isSomali

# ===== HEADER =====
st.title("SSM PRO")
st.subheader("Ku soo dhawoow Maal-gashiga" if st.session_state.isSomali else "Welcome to Investing")

st.button("U beddel Soomaali" if not st.session_state.isSomali else "Switch to English", on_click=toggle_lang)

# ===== LOGIN FORM =====
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("GAL APP-KA" if st.session_state.isSomali else "LOGIN")

if submitted:
    # Simulate login
    st.session_state.logged_in = True
    st.success(f"Welcome {username}!")

# ===== DASHBOARD =====
if st.session_state.get("logged_in", False):
    st.header("HANTIDA GUUD" if st.session_state.isSomali else "TOTAL WEALTH")
    balance = 1500.50
    st.metric("Balance", f"${balance:.2f}")

    st.subheader("Suuqa Live-ka ah" if st.session_state.isSomali else "Live Markets")
    btc_price = random.uniform(60000, 70000)
    st.metric("Bitcoin (BTC)", f"${btc_price:.2f}")

    # EVC PLUS helper
    with st.expander("KU SHUBO EVC PLUS" if st.session_state.isSomali else "DEPOSIT VIA EVC PLUS"):
        st.write("1. Garaac *712*" if st.session_state.isSomali else "1. Dial *712*")
        st.write("2. U dir lacagta: 061XXXXXXX" if st.session_state.isSomali else "2. Send money to: 061XXXXXXX")
        st.write("3. Nuqul ka qaado TXID-ga" if st.session_state.isSomali else "3. Copy the TXID")
