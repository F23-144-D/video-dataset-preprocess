#  ACTION DETECTION 
from ultralytics import YOLO
from parameters import trainModel, yamlFile, numEpochs, imageSize

# Train the model
results = trainModel.train(data=yamlFile, epochs=numEpochs, imgsz=imageSize)

