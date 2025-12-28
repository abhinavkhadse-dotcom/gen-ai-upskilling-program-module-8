import streamlit as st
import requests

st.title("FastAPI + Streamlit Demo")

number = st.number_input("Enter a number:", value=2)
# this is for external api calls
# if st.button("Calculate Square"):
#     response = requests.get(f"http://backend:8000/square/{number}")
#     data = response.json()
#     st.write(f"The square of {number} is {data['square']}")
if st.button("Calculate Square"):
    st.write(f"The square of {number} is {number**2}")
