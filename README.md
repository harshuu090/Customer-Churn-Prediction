<div align="center">

# 📞 Customer Churn Analysis & Prediction

### Predict Customer Churn Using Machine Learning

An end-to-end **Machine Learning** project that analyzes customer behavior and predicts the likelihood of customer churn using the **Telco Customer Churn Dataset**. The project includes **Exploratory Data Analysis (EDA)**, **Machine Learning model development**, and an interactive **Streamlit web application** for real-time predictions.

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-success?style=for-the-badge)

</p>

Predict customer churn, identify high-risk customers, and support data-driven retention strategies through machine learning.

</div>

---

# 📖 About The Project

**Customer Churn Analysis & Prediction** is a Machine Learning project developed to predict whether a telecom customer is likely to discontinue their service.

The project combines **Exploratory Data Analysis (EDA)** with **predictive modeling** to uncover customer behavior patterns and estimate churn probability. An interactive **Streamlit** application enables users to enter customer information and receive instant churn predictions along with a risk assessment.

This project demonstrates the complete machine learning workflow, from data preprocessing and model training to deployment in a user-friendly web application.

---

# 📂 Dataset

**Dataset:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

The dataset contains customer information including:

* Gender
* Senior Citizen Status
* Partner & Dependents
* Tenure
* Phone Service
* Internet Service
* Contract Type
* Payment Method
* Monthly Charges
* Total Charges
* Churn (Target Variable)

### 🎯 Target Variable

| Value | Meaning           |
| ----- | ----------------- |
| **1** | Customer Churned  |
| **0** | Customer Retained |

---

# 📊 Exploratory Data Analysis (EDA)

Several insights were obtained during data analysis:

* 📉 Customers with **Month-to-Month** contracts are more likely to churn.
* ⏳ Customers with shorter tenure have a higher churn probability.
* 🌐 Fiber Optic users exhibit higher churn rates compared to other internet service types.
* 💰 Higher monthly charges are associated with increased churn.
* 🤝 Customers on one-year or two-year contracts show stronger retention.

---

# 🤖 Machine Learning Model

### Model Used

* Logistic Regression

### Workflow

* Data Cleaning
* Missing Value Handling
* Feature Engineering
* Categorical Encoding
* Feature Scaling
* Train-Test Split
* Model Training
* Model Evaluation
* Feature Importance Analysis

---

# 📈 Model Evaluation

The model was evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1-Score

These metrics help assess the model's performance in predicting customer churn.

---

# 🌐 Streamlit Web Application

The project includes a responsive Streamlit application where users can:

* Enter customer information
* Predict customer churn in real time
* View churn probability
* Understand customer risk level
* Analyze important features influencing the prediction

---

# ✨ Features

* 📊 Interactive Customer Input Form
* 🤖 Real-Time Churn Prediction
* 📈 Churn Probability Score
* 🚦 Risk Categorization (Low / Medium / High)
* 📉 Feature Importance Visualization
* 💻 Simple and User-Friendly Interface
* ⚡ Fast Machine Learning Predictions

---

# 🛠 Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Analysis        |
| NumPy        | Numerical Computing  |
| Matplotlib   | Data Visualization   |
| Scikit-learn | Machine Learning     |
| Streamlit    | Web Application      |
| Pickle       | Model Serialization  |

---

# ⚙️ How It Works

1. Load and preprocess the customer dataset.
2. Clean and transform the data.
3. Train the Logistic Regression model.
4. Save the trained model using Pickle.
5. Launch the Streamlit application.
6. Enter customer details.
7. Generate churn prediction and probability.
8. Display the customer's risk category.

---

# 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── model/
│   ├── churn_model.pkl
│   └── encoder.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── notebooks/
    └── EDA.ipynb
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
```

Navigate to the project directory

```bash
cd customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

# 🎯 Use Cases

* Customer Retention Analysis
* Telecom Customer Analytics
* Churn Prediction
* Business Intelligence
* Machine Learning Demonstration
* Predictive Analytics
* Data Science Portfolio Projects

---

# 📈 Future Enhancements

* XGBoost & Random Forest Models
* Hyperparameter Optimization
* SHAP Explainability
* Interactive Dashboard
* Deployment on Streamlit Cloud
* Model Performance Comparison
* Customer Segmentation
* Deep Learning-Based Churn Prediction

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, improve the project, and submit a Pull Request.

---

# 👨‍💻 Developed By

## Harsh Kushwah

**Machine Learning Project**

Built with ❤️ using Python, Scikit-learn & Streamlit.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star on GitHub.

**Thank you for visiting! Happy Coding 🚀**

</div>
