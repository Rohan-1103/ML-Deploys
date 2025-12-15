import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Predictor")

# Slider input
house_size = st.slider(
    "Select house size (sqft):",
    min_value=300,
    max_value=3000,
    step=50
)

# Predict
if st.button("Predict Price"):
    prediction = model.predict([[house_size]])
    price_lakhs = prediction.item()

    if price_lakhs >= 100:
        price_crore = price_lakhs / 100
        st.success(f"Estimated Price: ₹ {price_crore:.2f} Crores")
    else:
        st.success(f"Estimated Price: ₹ {price_lakhs:.2f} Lakhs")
