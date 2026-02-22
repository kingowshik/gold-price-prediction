import streamlit as st
import pickle
import numpy as np

# Load model safely
model = pickle.load(open("gold_model.pkl", "rb"))

st.title("Gold Price Predictor")

usd = st.number_input("Enter USD/INR")

if st.button("Predict"):
    prediction = model.predict([[usd]])
    st.write(prediction)
