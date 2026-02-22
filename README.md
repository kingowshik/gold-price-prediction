# 💰 Gold Price Prediction using Linear Regression

A Machine Learning project that predicts **Gold Price (INR per gram)** based on the **USD/INR exchange rate**, with an interactive **Streamlit web application** for real-time predictions.

---

## 📖 Overview

Gold prices in India are closely related to the USD/INR exchange rate. This project uses **Linear Regression** to learn the relationship between these variables and estimate gold prices.

The project also includes a **Streamlit app** that allows users to input the USD/INR value and get instant predictions.

This project demonstrates a complete beginner-friendly ML workflow:

* Data Collection
* Data Analysis
* Model Training
* Model Evaluation
* Model Saving
* Web App Deployment

---

## 🧠 Model Information

**Algorithm Used:** Linear Regression
**Input Feature:** USD/INR exchange rate
**Output:** Gold price (₹ per gram)

### 📊 Performance

| Metric                  | Value |
| ----------------------- | ----- |
| R² Score                | 0.73  |
| Mean Absolute Error     | ₹816  |
| Root Mean Squared Error | ₹1021 |

---

## 🗂️ Repository Structure

```
gold-price-prediction-linear-regression
│
├── goldprediction.ipynb    # Jupyter notebook for training the model
├── gold_dataset.csv       # Dataset
├── gold_model.pkl         # Saved trained model
├── app.py                 # Streamlit application
├── requirements.txt      # Required libraries
└── README.md              # Project documentation
```

---

## 🚀 Streamlit Web Application

The project includes an interactive web interface.

### Features

* Enter USD/INR value
* Get instant gold price prediction
* Simple and clean interface

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/yourusername/gold-price-prediction-linear-regression.git
```

### 2. Navigate to the project folder

```
cd gold-price-prediction-linear-regression
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```
streamlit run app.py
```

---

## 📷 Example Prediction

| USD/INR | Predicted Gold Price |
| ------- | -------------------- |
| 88      | ₹7200 / gram         |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Pickle

---

## 🎯 Learning Outcomes

Through this project, I learned:

* How Linear Regression works
* How to train and evaluate ML models
* How to save and load trained models
* How to build ML web apps using Streamlit
* How to deploy ML projects on GitHub

---

## 🔮 Future Improvements

* Add more features to improve accuracy
* Use advanced ML algorithms
* Deploy app to cloud
* Integrate live gold price API

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Predictions may not reflect real market prices.

---

## 👨‍💻 Author

**Gowdham Subramaniyan**

Beginner Machine Learning Project

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
