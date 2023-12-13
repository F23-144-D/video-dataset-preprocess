#  ACTION DETECTION 
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.yaml')  # build a new model from YAML
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n-pose.yaml').load('yolov8n-pose.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='action_detection_model_config.yaml', epochs=100, imgsz=640)
