import streamlit as st
import pandas as pd

st.set_page_config(page_title="WiFi IDS Dashboard", layout="wide")
st.title("📶 WiFi Intrusion Detection System - Alert Dashboard")

try:
    df = pd.read_csv("intrusion_alerts.csv")
    st.dataframe(df[::-1], use_container_width=True)
except Exception as e:
    st.error(f"Could not load logs: {e}")
