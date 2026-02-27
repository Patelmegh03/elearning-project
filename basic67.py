import streamlit as st


st.header("manan")
st.subheader("AI domain")
st.write("infolabz,ahmedabad")
st.text("this is text")


name = "maggie"
st.write("what would you like:",name)

user = st.text_input("enter your name")
st.write("your name is:",user)

user1 = st.number_input("enter your age")
st.write("your age is:",user1)

skill = st.selectbox("select your skills",["AI","ML","DS"])
st.write("your skills is:",user)

mskill = st.multiselect("select your skills",["AI","ML","DS"])
st.write("select multiple skills here:",user)

sldbar = st.slider("rate your skill",1,10,5)
st.write("your rating is:",sldbar)

st.button("click me")


import streamlit as st
