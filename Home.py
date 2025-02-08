import streamlit as st

st.set_page_config(page_title="YOLO-TS Web App", layout="wide")

st.title("YOLO-TS: Traffic Sign Detection")
st.write("This web application utilizes the YOLO-TS model for traffic sign detection and classification.")

st.subheader("About YOLO-TS")
st.markdown("""
YOLO-TS is an advanced deep learning model for detecting and classifying road signs.
For more details, visit the [GitHub repository](https://github.com/Heqiang-Huang/YOLO-TS).
""")

# Sidebar Navigation Buttons
# st.sidebar.title("Navigation")

# if st.sidebar.button("🏠 Home"):
#     st.switch_page("app.py")  # If running locally, ensure this is the correct main script

# if st.sidebar.button("📤 Upload Image"):
#     st.switch_page("pages/1_Upload_Image.py")

# if st.sidebar.button("📊 View Results"):
#     st.switch_page("pages/2_View_Results.py")

st.sidebar.success("Use the buttons above to navigate.")
