from ultralytics import YOLO
print("lib loaded")
# Load a model
model = YOLO("yolov8n-pose.pt")  # load an official model
print("model loaded")
# Export the model
model.export(format="tfjs")
print("model exported")