# app.py

import streamlit as st
import calculator

st.title("Simple Calculator")

st.write("A basic calculator built with Streamlit 💻")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = calculator.add(num1, num2)
    elif operation == "Subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "Multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "Divide":
        result = calculator.divide(num1, num2)

    st.success(f"Result: {result}")
