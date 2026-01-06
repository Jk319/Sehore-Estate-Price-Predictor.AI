import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_PATH = os.path.join(BASE_DIR, "reports", "evaluation_report.pdf")

st.title("📊 Model Analytics & Report")
st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("R² Score", "0.87")
col2.metric("MAE", "₹1.2 Lakh")
col3.metric("RMSE", "₹2.1 Lakh")

st.divider()

if os.path.exists(REPORT_PATH):
    with open(REPORT_PATH, "rb") as file:
        st.download_button(
            "⬇️ Download Evaluation Report",
            file,
            file_name="Real_Estate_Model_Report.pdf",
            mime="application/pdf"
        )
else:
    st.warning("Report file not found.")
