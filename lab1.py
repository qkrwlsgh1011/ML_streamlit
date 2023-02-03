import streamlit as st

st.title("lab1")

file = st.file_uploader("upload_file")
file2 = st.camera_input("take picture")