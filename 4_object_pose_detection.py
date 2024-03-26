#performing object detection, pose estimation
from ultralytics import YOLO
import os
import glob

# Define the root directory
root_dir = './Dataset'
processed_dir_name = "/UCF-preprocessed"
output_dir_name = "/UCF_obj_detected"

processed_dir = root_dir + processed_dir_name

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Walk through all files in the directory
for dirpath, dirnames, filenames in os.walk(processed_dir):
    
    print("dirpath: ", dirpath)
    print("dirnames: ", dirnames)
    print("filenames: ", filenames)
        
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in glob.glob(os.path.join(dirpath, '*')) if os.path.splitext(file)[1].lower() in image_extensions]
    if len(image_files) == 0:
        continue

    # Create the output directory for the current action
    output_dir = dirpath.replace(processed_dir_name, output_dir_name)
    os.makedirs(output_dir, exist_ok=True)
    

    print("")
    print("")
    model.predict(source=dirpath, conf=0.5, save_txt=True, project=output_dir)
    print("completed model run on ", dirpath)
