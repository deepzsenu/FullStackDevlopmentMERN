import streamlit as st
import capitalfinder
st.title("This Application finds the Capital of the Place")

# st.subheader("Enter the Name of the place")

place = st.text_input("You Place here")

output = capitalfinder.capital_finder(place)
st.subheader("Capital")
st.write(output)