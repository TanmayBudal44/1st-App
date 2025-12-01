import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")
st.write("Enter numbers and choose an operation:")

# Inputs
num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number (ignored for single-operand functions)", value=0.0)

# Operation Categories
operation_type = st.selectbox(
    "Select Type",
    ("Basic", "Scientific (Single Number)", "Scientific (Two Numbers)")
)

# Operation Select
if operation_type == "Basic":
    operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))

elif operation_type == "Scientific (Single Number)":
    operation = st.selectbox(
        "Operation",
        (
            "Square",
            "Square Root",
            "Cube",
            "Cube Root",
            "Sin",
            "Cos",
            "Tan",
            "Log (base 10)",
            "Natural Log (ln)",
            "Factorial"
        )
    )

elif operation_type == "Scientific (Two Numbers)":
    operation = st.selectbox(
        "Operation",
        ("Power (x^y)", "Modulus (x % y)")
    )

# Calculate Button
if st.button("Calculate"):
    try:
        # BASIC OPERATIONS
        if operation_type == "Basic":
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 == 0:
                    result = "❌ Cannot divide by zero"
                else:
                    result = num1 / num2

        # SINGLE-NUMBER SCIENTIFIC OPERATIONS
        elif operation_type == "Scientific (Single Number)":
            if operation == "Square":
                result = num1 ** 2
            elif operation == "Square Root":
                result = math.sqrt(num1)
            elif operation == "Cube":
                result = num1 ** 3
            elif operation == "Cube Root":
                result = num1 ** (1/3)
            elif operation == "Sin":
                result = math.sin(math.radians(num1))
            elif operation == "Cos":
                result = math.cos(math.radians(num1))
            elif operation == "Tan":
                result = math.tan(math.radians(num1))
            elif operation == "Log (base 10)":
                result = math.log10(num1)
            elif operation == "Natural Log (ln)":
                result = math.log(num1)
            elif operation == "Factorial":
                if num1 < 0 or int(num1) != num1:
                    result = "❌ Factorial only works for non-negative integers"
                else:
                    result = math.factorial(int(num1))

        # TWO-NUMBER SCIENTIFIC OPERATIONS
        elif operation_type == "Scientific (Two Numbers)":
            if operation == "Power (x^y)":
                result = num1 ** num2
            elif operation == "Modulus (x % y)":
                result = num1 % num2

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")
