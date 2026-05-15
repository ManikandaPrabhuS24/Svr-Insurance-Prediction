import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Load trained model
model = pickle.load(open("Finalized_svr_model.sav", "rb"))

# App title
st.title("Medical Insurance Cost Prediction using (Support Vector Regression)")

st.write("Enter customer details to predict insurance charges.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

sex = st.selectbox("Gender", ["Female", "Male"])

smoker = st.selectbox("Smoker", ["No", "Yes"])

# Convert categorical values
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

# Prediction button
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame([[age, bmi, children, sex_male, smoker_yes]],
                              columns=['age', 'bmi', 'children', 'sex_male', 'smoker_yes'])

    input_scaled = sc.fit_transform(input_data)
    prediction = model.predict(input_scaled)
    

    st.success(f"Predicted Insurance Cost: Rs./ {prediction[0]:,.2f}")