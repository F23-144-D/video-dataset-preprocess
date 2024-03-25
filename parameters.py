from ultralytics import YOLO

#1_frame_extraction
#frames per second to extract
FPS_RATE = 1

#2_writing_frame_data
#none

#3_data_preprocessing
#frames per video
CLIP_LENGTH = 8

#4_object_pose_detection
# Load a pretrained YOLOv8n model
detectModel = YOLO('yolov8n-pose.pt')

#5_action_labelling
#either ROI or pose estimation
APPLY_ROI = False

#6_data_train_test_splitting
#none

#7_action_detection_model_training
# Load a model
trainModel = YOLO('yolov8n-pose.yaml')  # build a new model from YAML
trainModel = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
trainModel = YOLO('yolov8n-pose.yaml').load('yolov8n-pose.pt')  # build from YAML and transfer weights
yamlFile = 'action_detection_model_config.yaml'
numEpochs = 10
imageSize = 640
