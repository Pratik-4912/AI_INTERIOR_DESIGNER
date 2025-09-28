from ultralytics import YOLO
from PIL import Image

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")  # free small model

def detect_room_objects(image):
    # Convert PIL to OpenCV
    results = model.predict(image)
    objects = [str(obj.cls) for obj in results[0].boxes]  # detected classes
    return objects
