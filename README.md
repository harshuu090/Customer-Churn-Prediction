#Customer Churn Analysis & Prediction
📌 Project Overview

This project focuses on analyzing and predicting customer churn using the Telco Customer Churn dataset.
The objective is to identify customers who are likely to leave the telecom service and help businesses take proactive retention actions.

The project includes:
📊 Exploratory Data Analysis (EDA)
🤖 Machine Learning Model Training
🌐 Interactive Streamlit Web Application
🚀 Deployment-ready architecture

📂 Dataset
Dataset used: WA_Fn-UseC_-Telco-Customer-Churn.csv
It contains customer information such as:

Gender
Senior Citizen status
Partner & Dependents
Tenure
Contract Type
Internet Service
Monthly Charges
Total Charges
Churn (Target Variable)

Target Variable:
1 → Customer Churned
0 → Customer Stayed

📊 Exploratory Data Analysis (EDA)

Key insights from analysis:
Customers with Month-to-month contracts churn more.
Low tenure customers have higher churn probability.
Fiber optic users show higher churn rate.
Higher Monthly Charges increase churn likelihood.
Customers with long-term contracts (1 or 2 years) are more loyal.

🤖 Machine Learning Model

Model Used:
Logistic Regression

Steps performed:
Data cleaning & preprocessing
Encoding categorical variables
Train-Test split
Model training
Performance evaluation
Feature importance extraction
Evaluation Metrics:
Accuracy Score
Confusion Matrix
Classification Report

🌐 Streamlit Web Application
An interactive web app was built using Streamlit where users can:

Enter customer details

Get churn probability

View risk category (Low / Medium / High)

See top important features affecting churn

🔥 Features of the App
Real-time churn prediction
Probability-based risk categorization
Feature importance visualization
Clean and professional UI

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Streamlit
Pickle

🚀 How to Run Locally
Clone the repository:

git clone <your-repo-link>
cd telco-churn-app

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py
