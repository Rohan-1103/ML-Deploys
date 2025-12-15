import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Predictor")

# Input
house_size = st.number_input("Enter house size (sqft):", min_value=300)

# Predict
if st.button("Predict Price"):
    prediction = model.predict([[house_size]])
    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")
