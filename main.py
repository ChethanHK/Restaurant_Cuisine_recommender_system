from langchain_helper import generate_restaurant_name_and_items
import langchain_helper
import streamlit as st

st.title("Restaurant name Generator")

cuisine=st.sidebar.selectbox("pick a cuisine",("Indian","Italian","Mexican","Arabian","Japanese"))


if cuisine:
    response=langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu'].strip().split(",")
    st.write("**menu_items**")
    for item in menu_items:
        st.write("-",item)