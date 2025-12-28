# 🏠 House Price Predictor using Machine Learning & Streamlit

A simple end-to-end Machine Learning web application that predicts house prices based on house size (in square feet).  
The model is trained using **Linear Regression** and deployed using **Streamlit**, providing an interactive UI for real-time predictions with accuracy of 93%.

---

## 🚀 Live Demo

👉 https://slr-house-price-app.streamlit.app/

---

## 📌 Features

- 📊 Predicts house price from house size
- 🎚️ Interactive slider input
- 💰 Displays price in Lakhs & Crores
- ⚡ Fast and lightweight Streamlit UI
- 🌐 Deployed online for public access

---

## 🧠 Machine Learning Model

- Algorithm: **Linear Regression**
- Library: `scikit-learn`
- Trained on: Sample housing dataset
- Input Feature: `House Size (sqft)`
- Output: `Estimated Price`

The trained model is saved as a `.pkl` file and loaded into the Streamlit app for inference.

---

## 🗂️ Project Structure
ML-Deploys/<br>
└── SimpleLinearRegression/<br>
├── app.py<br>
├── model.pkl<br>
├── requirements.txt<br>
└── README.md<br>

---

## ⚙️ Run Locally

Clone the repo:

```bash
git clone https://github.com/Rohan-1103/ML-Deploys.git
cd ML-Deploys/SimpleLinearRegression
```

## Install dependencies
``` bash
pip install -r requirements.txt
```

## Run the app
``` bash
streamlit run app.py
```
