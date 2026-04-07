import streamlit as st
import sqlite3
import pandas as pd
import requests

# --- APP CONFIG ---
st.set_page_config(page_title="SSM Investment Pro", layout="wide")

st.title("🚀 SSM Global Investment Suite")

# --- DASHBOARD ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Balance", value="$1,000.00")
with col2:
    st.info("Verified Account ✅")

st.subheader("Market Trend")
# Tusaale Jaantus ah
data = pd.DataFrame({'Days': range(10), 'Price': [45, 48, 47, 50, 52, 55, 54, 58, 60, 62]})
st.line_chart(data.set_index('Days'))

if st.button("Buy BTC Now"):
    st.success("Transaction Processed!")
