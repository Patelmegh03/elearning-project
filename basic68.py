import streamlit as st
from datetime import date
from streamlit import date_input, checkbox

with st.form(key="form1"):
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password",type="password")
    date_input = st.date_input("Enter your birthdate")
    checkbox = st.checkbox("I agree with terms and conditions")
    if checkbox:
        st.write("You agreed")
    radio_option =st.radio("Select your gender",("Male","Female","other"))

    uplode_file = st.file_uploader("Upload your file",type=["jpg","png","pdf"])
    if uplode_file is not None:
        st.write("File is uploaded successfully",uplode_file.name)
    btn = st.form_submit_button(label="Submit")
    if btn:
        st.write("Email is",email)
