# !yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=25 imgsz=800 plots=True




from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose')  # load a pretrained model

# Train the model
model.train(data='custom_data.yaml', batch=8, epochs=100, imgsz=640)
