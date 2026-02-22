import streamlit as st
import pickle
import numpy as np

# Load model
with open("gold_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Gold Price Estimator", layout="centered")

st.title("💰 Gold Price Estimator")
st.write("Estimate gold price (₹ per gram) based on USD/INR exchange rate")

usd_inr = st.number_input(
    "Enter USD/INR value",
    min_value=50.0,
    max_value=120.0,
    value=88.0,
    step=0.1
)

if st.button("Predict Gold Price"):
    prediction = model.predict([[usd_inr]])[0]
    st.success(f"Estimated Gold Price: ₹{prediction:.2f} per gram")

st.warning(
    "⚠️ This model is for educational purposes only. "
    "Predictions outside the training range may be unreliable."
)