import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

model = joblib.load("linreg_model.pkl")

df = pd.read_csv("insurance.csv")
df['sex'] = df['sex'].map({'male': 1, 'female': 0})
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
df['region_number'] = df['region'].astype('category').cat.codes

X = df[['age', 'bmi', 'smoker', 'children', 'region_number']]
y = df['charges']

model = LinearRegression()
model.fit(X, y)

def calculate_risk(age, bmi, smoker):
    risk = round(age * 0.2 + bmi * 0.3 + smoker * 30, 2)
    if risk < 20:
        category = 'Low'
    elif risk < 40:
        category = 'Medium'
    else:
        category = 'High'
    return risk, category

st.title("Insurance Risk Analyzer")

age = st.number_input("Age", min_value=0, max_value=100, value=30)
sex = st.selectbox("Sex", ['male', 'female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.selectbox("Smoker", ['yes', 'no'])
children = st.number_input("Number of children", min_value=0, max_value=10, value=0)
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])

if st.button("Calculate"):
    sex_code = 1 if sex == 'male' else 0
    smoker_code = 1 if smoker == 'yes' else 0
    region_code = {'southeast': 2, 'southwest': 3, 'northeast': 1, 'northwest': 0}[region]

    X_new = np.array([[age, bmi, smoker_code, children, region_code]])
    predicted_charge = model.predict(X_new)[0]

    risk_score, category = calculate_risk(age, bmi, smoker_code)

    st.success(f"Estimated Risk Score: **{risk_score}** ({category} Risk)")
    st.success(f"Predicted Medical Charges: **${predicted_charge:,.2f}**")