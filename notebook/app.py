import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Telco Churn App", layout="centered")

st.title("📞 Customer Churn Prediction")

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# ---------- USER INPUTS ----------

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
phoneservice = st.selectbox("Phone Service", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthlycharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
totalcharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# ---------- PREDICTION BUTTON ----------

if st.button("Predict Churn"):

    user_input = {
        "SeniorCitizen": senior,
        "tenure": tenure,
        "MonthlyCharges": monthlycharges,
        "TotalCharges": totalcharges,
        "gender_" + gender: 1,
        "Partner_" + partner: 1,
        "Dependents_" + dependents: 1,
        "PhoneService_" + phoneservice: 1,
        "InternetService_" + internet: 1,
        "Contract_" + contract: 1,
    }

    input_df = pd.DataFrame([user_input])

    # Match training columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    prob = probability[0][1] * 100

    st.write("### 📊 Churn Probability:", round(prob, 2), "%")

    # Risk Category
    if prob < 30:
        st.success("🟢 Low Risk Customer")
    elif prob < 60:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.error("🔴 High Risk Customer")

    # Final Prediction
    if prediction[0] == 1:
        st.error("❌ Customer Will Churn")
    else:
        st.success("✅ Customer Will Stay")

# ---------- FEATURE IMPORTANCE SECTION ----------

st.markdown("---")
st.subheader("📊 Top 10 Important Features")

importance = model.coef_[0]
features = model_columns

feature_importance = pd.Series(importance, index=features)
top_features = feature_importance.abs().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
top_features.sort_values().plot(kind="barh", ax=ax)
plt.title("Top 10 Features Affecting Churn")

st.pyplot(fig)