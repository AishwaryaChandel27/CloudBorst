import streamlit as st
import pickle

# Load the background image and set page styling
page = """
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f0f2f6;
}
.stTextInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.7);
}
.stNumberInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.7);
}
.stButton > button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.stButton > button:hover {
    background-color: #45a049;
}
</style>
"""
st.markdown(page, unsafe_allow_html=True)

# Load the trained model
model = pickle.load(open("cbmodel.pkl", "rb"))

# Set title and input fields
st.title("CloudBurst Predictor")
st.subheader("Enter the following parameters:")

input_tem = st.number_input("Temperature (°C)")
input_atem = st.number_input("Apparent Temperature (°C)")
input_hum = st.number_input("Humidity (%)")
input_ws = st.number_input("Wind Speed (km/h)")
input_wb = st.number_input("Wind Bearing (°)")
input_vis = st.number_input("Visibility (km)")
input_pre = st.number_input("Pressure (mb)")

# Predict cloudburst based on input
if st.button("Predict"):
    pred = [[input_tem, input_atem, input_hum, input_ws, input_wb, input_vis, input_pre]]
    result = model.predict(pred)
    st.subheader("Prediction Result:")
    if result == 0:
        st.error("Risk of Cloudburst is high.")
    else:
        st.success("No risk of Cloudburst.")
