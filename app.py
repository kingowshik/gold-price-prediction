import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Gold Price Prediction",
    page_icon="💰",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    with open("gold_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# -----------------------------
# UI Design
# -----------------------------

# Title
st.title("💰 Gold Price Prediction App")

# Subtitle
st.markdown(
    "Predict **Gold Price (₹ per gram)** based on **USD/INR exchange rate** using Machine Learning."
)

st.divider()

# Input Section
st.subheader("📥 Enter Input")

usd_inr = st.number_input(
    "USD/INR Exchange Rate",
    min_value=50.0,
    max_value=120.0,
    value=88.0,
    step=0.1,
    help="Enter current USD to INR exchange rate"
)

# Predict Button
if st.button("🔮 Predict Gold Price", use_container_width=True):

    prediction = model.predict([[usd_inr]])

    st.success(f"✅ Estimated Gold Price: ₹ {prediction[0]:.2f} per gram")

# -----------------------------
# Extra Information
# -----------------------------

st.divider()

st.subheader("ℹ️ About this Project")

st.write("""
This Machine Learning model predicts gold price using Linear Regression.

**Input:**
- USD/INR exchange rate

**Output:**
- Gold price in Indian Rupees per gram
""")

# Footer
st.divider()

st.caption("Created by Gowshik Subramaniyan | Machine Learning Project")
