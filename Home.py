import streamlit as st
import pandas as pd
import joblib
import os

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "E:\Sehore_RealEstate_WebApp\RealEstate-Price-Prediction\models\final_real_estate_model.pkl")

# ---------- LOAD MODEL ----------
model = joblib.load(MODEL_PATH)

# ---------- UI ----------
st.title("🏠 Property Price Prediction")
st.markdown("Predict market value using ML-based valuation model")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    district = st.selectbox("District", ["Sehore"])
    tehsil = st.selectbox("Tehsil", ["Rehti", "Jawar", "Budhni", "Ichhawar"])
    village = st.text_input("Village / Town")

with col2:
    property_type = st.selectbox(
        "Property Type",
        ["Residential", "Commercial", "Industrial", "Agricultural"]
    )
    ownership = st.selectbox(
        "Ownership",
        ["Private", "Government", "Institutional"]
    )
    road_access = st.selectbox("Road Access", ["Yes", "No"])

with col3:
    size = st.slider("Size (sq meter)", 100, 10000, 500)
    population = st.number_input("Population", min_value=500, value=3000)
    amenities = st.slider("Amenities", 1, 15, 5)

st.divider()

col4, col5, col6 = st.columns(3)

with col4:
    stamp = st.slider("Stamp Duty (%)", 2.0, 10.0, 5.0)
with col5:
    registration = st.slider("Registration (%)", 1.0, 5.0, 2.0)
with col6:
    broker = st.slider("Broker (%)", 0.0, 5.0, 2.0)

distance = st.slider("Nearest Neighborhood Distance (km)", 0.5, 15.0, 5.0)

# ---------- PREDICTION ----------
if st.button("🔮 Predict Market Price", use_container_width=True):

    input_df = pd.DataFrame([{
        "District": district,
        "Tehsil": tehsil,
        "Village/Town": village,
        "Property_Type": property_type,
        "Ownership": ownership,
        "Size_sq_m": size,
        "Stamp_Duty%": stamp,
        "Registration%": registration,
        "Broker%": broker,
        "Population": population,
        "Amenities": amenities,
        "Road_Access": road_access,
        "Nearest_Neigh_km": distance
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Market Price: ₹ {prediction:,.0f}")
