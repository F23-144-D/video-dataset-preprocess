!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=25 imgsz=800 plots=True









from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.yaml').load('yolov8n.pt')  # load a pretrained model

# Train the model
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)





import os
from ultralytics import YOLO

# Define the path to your YOLOv8n-pose configuration file
config_path = 'path/to/yolov8n-pose.yaml'

# Load the YOLO model with the specified configuration file
model = YOLO(config_path)

# Define the path to your UCF.yaml file
ucf_config_path = 'path/to/UCF.yaml'

# Train the model using the specified UCF.yaml file
results = model.train(data=ucf_config_path, epochs=100, imgsz=640)
