import streamlit as st

st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.sidebar.title("🏠 Real Estate App")
page = st.sidebar.radio(
    "Navigation",
    ["Property Price Prediction", "Market Analytics"]
)

if page == "Property Price Prediction":
    import streamlit_app.Home

else:
    import streamlit_app.analytics

