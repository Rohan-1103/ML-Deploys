# ⛽ Petrol Consumption Prediction App

A Machine Learning web application built with **Streamlit** that predicts **petrol consumption** based on key economic and infrastructure factors, with almost perfect accuracy.  
The model is trained using Multiple Linear Regression and deployed as an interactive web app.

---

## 🚀 Live Demo

👉 https://petrol-consumption.streamlit.app/  

---

## 📌 Project Overview

This project demonstrates an end-to-end ML deployment workflow:

- Data preprocessing & feature selection  
- Training a regression model on petrol consumption data  
- Saving the trained model using Pickle  
- Building an interactive UI using Streamlit  
- Deploying the app on Streamlit Community Cloud  

Users can adjust feature values using sliders and instantly get predictions.

---

## ✨ Features

- 🎚️ Sidebar sliders for input features  
- 📊 Real-time petrol consumption prediction  
- 📋 Displays selected input values  
- 🧠 Uses trained ML regression model  
- 🌐 Web-based & easy to use  
- ⚡ Robust file loading using absolute paths  

---

## 🧠 Model & Dataset Information

The model predicts petrol consumption using the following features:

| Feature | Description | UI Range |
|--------|-------------|----------|
| `Petrol_tax` | Tax on petrol | 5 – 10 |
| `Average_income` | Average income of population | 3000 – 5500 |
| `Paved_Highways` | Miles of paved highways | 0 – 18000 |
| `Population_Driver_licence(%)` | % of population with driving license | 0 – 100 |

- Target: `Petrol_Consumption`  
- Algorithm: **Multiple Linear Regression**  
- Library: `scikit-learn`  
- Model file: `petrol_consumption_model.pkl`

> Note: Percentage input is shown as 0–100% in UI and internally converted to 0–1 for model inference.

---

## 🗂️ Project Structure
FuelConsumptionPrediction_MLR/ <br>
├── petrol_app.py                     # Streamlit application <br>
├── petrol_consumption_model.pkl      # Trained ML model <br>
├── requirements.txt                  # Dependencies <br>
└── README.md                         # Documentation <br>


---

## ⚙️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Rohan-1103/ML-Deploys.git
cd ML-Deploys/FuelConsumptionPrediction_MLR
```

### 2️⃣ Install Dependencies
``` bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
``` bash
streamlit run petrol_app.py
```
