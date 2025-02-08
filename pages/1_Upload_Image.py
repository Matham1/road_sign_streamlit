import streamlit as st
import os

st.title("Upload an Image")

uploaded_file = st.file_uploader("Choose a .jpg image", type=["jpg"])

if uploaded_file is not None:
    # Save the file temporarily
    file_path = os.path.join("uploaded_image.jpg")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")
    st.session_state["uploaded_image"] = file_path

    # Button to proceed
    if st.button("Proceed to Results"):
        st.switch_page("pages/2_Results.py")

