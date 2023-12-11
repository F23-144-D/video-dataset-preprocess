#performing object detection, pose estimation

from PIL import Image
from ultralytics import YOLO
import cv2
import os
import time
from datetime import datetime


# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Define the root directory
root_dir = 'Dataset/UCF101_n_frames'

# Common output root directory
output_root = 'objdetect'
os.makedirs(output_root, exist_ok=True)

# Get a list of directories (actions) in the root directory
action_directories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
# print(action_directories, "....................is action directories")



def objdetector(dirpath):
    # print("#####################################################################")
    # print("dir path: " , dirpath)
    # print("dir name: " , dirnames)
    # print("")
    # print("file path: " , filenames)
    print("")
    print("")
    model.predict(source=dirpath, conf=0.5, save_txt=True, project=output_dir)
    print("completed model run on ", dirpath)

#%%

# Iterate through each action directory
for action_dir in action_directories:



    # Create the output directory for the current action
    output_dir = os.path.join(output_root, f'{action_dir}')
    os.makedirs(output_dir, exist_ok=True)

    # Print the current action directory
    print(f"Processing action--------------------------------: {action_dir}")

    # Process the current action directory
    action_path = os.path.join(root_dir, action_dir)

    # Walk through all files in the directory
    i = 1
    for dirpath, dirnames, filenames in os.walk(action_path):


        


        # i = i + 1
        # if i == 10:
        #     break
        if i == 1:
            i = 2
            continue

        
        objdetector(dirpath)
        # time.sleep(5)  # Wait for 5 seconds
