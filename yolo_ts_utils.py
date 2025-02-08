import cv2
import numpy as np
import sys
from pathlib import Path

yolo_ts_path = str(Path(__file__).parent.parent / "YOLO-TS")
if yolo_ts_path not in sys.path:
    sys.path.append(yolo_ts_path)

# Now you can import ultralytics
from ultralytics import YOLO
import torch
from ultralytics.nn.tasks import torch_safe_load

# Monkey-patch the YOLO-TS load function
def patched_torch_safe_load(file):
    return torch.load(file, map_location="cpu", weights_only=False), file

# Replace the original function with the patched version
from ultralytics.nn import tasks
tasks.torch_safe_load = patched_torch_safe_load

# Now load the model
from ultralytics import YOLO
MODEL_PATH = "best.pt"
model = YOLO(MODEL_PATH)


def run_yolo_ts(image_path):
    """
    Runs YOLO-TS on an input image and returns annotated image and detections.
    """
    # Load image
    image = cv2.imread(image_path)
    
    # Run inference
    results = model(image_path)  
    
    # Process results
    detections = []
    output_image = image.copy()

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box
            conf = float(box.conf[0])  # Confidence score
            cls = int(box.cls[0])  # Class index
            class_name = model.names[cls]  # Get class name

            # Save detection
            detections.append({"class": class_name, "confidence": conf})

            # Draw bounding box
            cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(output_image, f"{class_name} ({conf:.2f})",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return output_image, detections
