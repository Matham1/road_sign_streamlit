import streamlit as st
import cv2
import numpy as np
import yolo_ts_utils

import os

import sys
from pathlib import Path

# Add the YOLO-TS directory to the Python path
yolo_ts_path = str(Path(__file__).parent.parent / "YOLO-TS")
if yolo_ts_path not in sys.path:
    sys.path.append(yolo_ts_path)

# Now you can import ultralytics
from ultralytics import YOLO


st.title("YOLO-TS Detection Results")

if "uploaded_image" in st.session_state:
    file_path = st.session_state["uploaded_image"]

    # Load image
    image = cv2.imread(file_path)
    st.image(image, caption="Uploaded Image", width=640)  # Change width here

    # Run YOLO-TS detection
    output_image, detections = yolo_ts_utils.run_yolo_ts(file_path)

    st.subheader("Detection Results")
    st.image(output_image, caption="YOLO-TS Annotated Image", width=640)  # Adjust width
    st.write("Detected Signs:")

    for det in detections:
        st.write(f"**{det['class']}** - Confidence: {det['confidence']:.2f}")
else:
    st.warning("Please upload an image first from the Upload Image page.")
