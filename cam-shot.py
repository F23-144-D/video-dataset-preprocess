from ultralytics import YOLO


model=YOLO("t13-pose.pt")
results= model.predict(source="0", show=True)

print (results)