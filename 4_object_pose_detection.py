#performing object detection, pose estimation
from ultralytics import YOLO
import os
import glob


# Define the root directory
root_dir = '/workspaces/video-dataset-preprocess/Dataset'
processed_data_dir = "/UCF-preprocessed"
output_dir = "/UCF_obj_detected"


# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Walk through all files in the directory
for dirpath, dirnames, filenames in os.walk(root_dir + processed_data_dir):
    
    print("dirpath: ", dirpath)
    print("dirnames: ", dirnames)
    print("filenames: ", filenames)
        
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in glob.glob(os.path.join(dirpath, '*')) if os.path.splitext(file)[1].lower() in image_extensions]
    if len(image_files) == 0:
        continue

    # Create the output directory for the current action
    output_dir = dirpath.replace(processed_data_dir, output_dir)
    os.makedirs(output_dir, exist_ok=True)
    

    print("")
    print("")
    model.predict(source=dirpath, conf=0.5, save_txt=True, project=output_dir)
    print("completed model run on ", dirpath)
