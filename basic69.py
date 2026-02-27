import pandas as pd
from streamlit_option_menu import option_menu
import streamlit as st

with st.sidebar:
    selected = option_menu("Admin Panel",["Dashboard","About us",""
                                                                 "Dataset","Project","Login","settings"],
                           icons=["cast","people","table","activity","lock","gear"],
                           menu_icon=["cast"],default_index=0,orientation="vertical")
if selected =="Dashboard":
        st.header("Project Name")
        st.write("project description")

if selected == "Dataset":
        st.header("Dataset")
        df = pd.read_csv("mall_csv")
        st.dataframe(df)

if selected == "Login":
    st.header("Login")
    with st.form(key="form1"):
      user = st.text_input("Enter your username")
      password = st.text_input("enter your password",type="password")
      submitbtn = st.form_submit_button(label="Submit")
    if submitbtn:
        if user == "abc123" and password == "1234":
            st.success("Login successfully")
        else:
            st.error("Invalid details")


if selected == "settings":
    st.header("setting")
    st.info("This is under development")





