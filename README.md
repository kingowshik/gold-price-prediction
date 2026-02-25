# 💰 Gold Price Prediction
🔗 **Live App:** https://gold-price-prediction-mdwwkuvswmx2o9popya7ry.streamlit.app/

A Machine Learning project that predicts **Gold Price (₹ per gram)** based on the **USD/INR exchange rate** using **Linear Regression**, with an interactive **Streamlit web application**.

---

## 📖 Overview

Gold prices in India are influenced by global economic factors, especially the USD/INR exchange rate. This project builds a Linear Regression model to predict gold prices based on the exchange rate.

This project demonstrates a complete Machine Learning workflow:

* Data loading and preprocessing
* Model training using Linear Regression
* Model evaluation
* Saving the trained model
* Building a web app using Streamlit

---

## 🧠 Model Details

**Algorithm:** Linear Regression

**Input:**

* USD/INR exchange rate

**Output:**

* Gold price (₹ per gram)

**Performance:**

* R² Score: 0.73
* Mean Absolute Error: ₹816
* Root Mean Squared Error: ₹1021

---

## 📁 Project Structure

```id="py80sn"
gold-price-prediction
│
├── goldprediction.ipynb
├── gold_dataset.csv
├── gold_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Streamlit Application

This project includes a web application where users can:

* Enter USD/INR value
* Get instant gold price prediction

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```id="7po2i8"
git clone https://github.com/kingowshik/gold-price-prediction.git
```

### Step 2: Open project folder

```id="u4ww5c"
cd gold-price-prediction
```

### Step 3: Install libraries

```id="9jhtav"
pip install -r requirements.txt
```

### Step 4: Run Streamlit app

```id="2l04xg"
streamlit run app.py
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Pickle

---

## 📊 Example

Input:

```id="j3a6xg"
USD/INR = 88
```

Output:

```id="85x7q4"
Predicted Gold Price ≈ ₹7200 per gram
```

---

## 🎯 Project Purpose

This is a beginner Machine Learning project created to learn:

* Linear Regression
* Model training and evaluation
* Model deployment
* Building ML web applications

---

## ⚠️ Disclaimer

This project is for educational purposes only and should not be used for real financial decisions.

---

## 👨‍💻 Author

**Gowshik Subramaniyan**

---

## ⭐ If you like this project

Please give it a ⭐ on GitHub.
