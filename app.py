import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("pima_diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.title("Pima Indian Diabetes Prediction")
st.write("""
This application predicts whether a person has diabetes based on medical data. 
Input the details below to get the prediction.
""")

# Input form
def user_input_features():
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, step=1)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, step=1)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, step=1)
    insulin = st.number_input("Insulin Level (IU/mL)", min_value=0, step=1)
    bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
    age = st.number_input("Age (years)", min_value=0, step=1)
    
    features = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]).reshape(1, -1)
    return features

# Predict button
input_data = user_input_features()
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
    st.subheader(f"Prediction: {result}")
