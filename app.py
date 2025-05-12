import streamlit as st

st.title("LSTM Time Series Predictor")

data = st.text_input("Enter data points (comma-separated):")
if data:
    try:
        points = list(map(float, data.split(",")))
        st.write("You entered:", points)
        # You can load your model and add prediction code here
    except:
        st.error("Invalid input. Please enter comma-separated numbers.")
