import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("customer_churn.pkl", "rb"))

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", ['Male', 'Female'])
tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

gender = 1 if gender == 'Male' else 0

input_data = np.array([[gender, tenure, monthly, total]])  
prediction = model.predict(input_data)

if prediction[0] == 1:
    st.warning("🟡 This customer is likely to churn.")
else:
    st.success("🟢 This customer is likely to stay.")
