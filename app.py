import streamlit as st
import pandas as pd

from Utils import *
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

def display_table_without_index(data):
    df = pd.DataFrame(list(data.items()), columns=['Attribute', 'Value'])
    st.table(df)


st.title("License Plate Information")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


license_plate_input = st.text_input("Enter License Plate Number:")

if license_plate_input:
    info1, info2 = getInfo(license_plate_input)
    if info1:
        st.subheader("Vehicle Information")
        display_table_without_index(info1)
        st.subheader("Additional Information")
        display_table_without_index(info2)
    else:
        st.warning("Please enter a valid Indian license plate number.")

