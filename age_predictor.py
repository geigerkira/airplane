import streamlit as st
import pandas as pd
import joblib

import os
os.chdir(os.path.dirname(__file__))



# Modell betöltése
model = joblib.load('model.pkl')

# Cím és leírás
st.title("Age Predictor App")
st.write("Ez az alkalmazás az utas jellemzői alapján prediktálja az életkor kategóriáját.")

# Input mezők
st.header("Adatok bevitele:")
customer_type = st.selectbox("Customer Type", [0, 1], format_func=lambda x: "Loyal" if x == 0 else "Disloyal")
type_of_travel = st.selectbox("Type of Travel", [0, 1], format_func=lambda x: "Personal" if x == 0 else "Business")
class_business = st.selectbox("Business Class", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
online_boarding = st.slider("Online Boarding", 0, 5, 3)  # Csúszka 0-tól 5-ig
flight_distance = st.number_input("Flight Distance", min_value=0, max_value=5000, value=1000)

# Inputok dataframe-be alakítása
input_data = pd.DataFrame({
    'Customer Type': [customer_type],
    'Type of Travel': [type_of_travel],
    'Class_Business': [class_business],
    'Online boarding': [online_boarding],
    'Flight Distance': [flight_distance]
})

# Predikció futtatása
if st.button("Prediktálás"):
    prediction = model.predict(input_data)
    age_category = ["Fiatal", "Középkorú", "Idősebb"]
    st.success(f"Prediktált életkor kategória: {age_category[prediction[0]]}")
