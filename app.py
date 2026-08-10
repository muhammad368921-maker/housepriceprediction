import streamlit as st
import joblib
model = joblib.load("house_price_model.pkl")

st.title("HOUSE PRICE PREDICTION")
st.write("Enter the house detail below to estimate its price")
st.divider()
col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Average Area Income",
    min_value=17796.63,
    max_value=107701.75,
    value=68583.11,
    step=1000.0)
st.write("Income entered:",income)
with col2:
    house_age = st.number_input("Average Area House Age",
    min_value=2.64,
    max_value=9.52,
    value=5.98,
    step=0.1)
st.write("House Age Entered:",house_age)
col3, col4 = st.columns(2)
with col3:
    room = st.number_input("Average Number of Room",
    min_value=3.24,
    max_value=10.76,
    value=6.99,
    step=0.1)
st.write("Number of rooms:",room)
with col4:
    badrooms = st.number_input("Average Number of badrooms",
    min_value=2.0,
    max_value=6.5,
    value=4.0,
    step=0.1)
st.write("number od badrooms:",badrooms)
population = st.number_input("Area population",
    min_value=172.61,
    max_value=69621.71,
    value=36163.52,
    step=100.0)
st.write("Area population:",population)
if st.button("predict House price"):
    st.write("income:",income)
    st.write("House age:",house_age)
    st.write("rooms:",room)
    st.write("bedrooms:",badrooms)
    st.write("population:",population)
    prediction = model.predict([[income,house_age,room,badrooms,population]])
    price = prediction[0]
    st.success(f"Estimated House price: {price:,.2f} ")
    st.caption("Prediction generated using a trained linear regression model.")
   