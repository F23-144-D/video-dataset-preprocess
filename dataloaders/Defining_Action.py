#----------------------------------------MANUAL------------------------------

import os
import shutil

# Define the source folder containing all action folders
source_folder = './Dataset/UCF-yolo'

# Define the destination folders for normal and abnormal actions
normal_action_folder = './Action/NormalAction'
abnormal_action_folder = './Action/AbnormalAction'

# Create destination folders if they don't exist
os.makedirs(normal_action_folder, exist_ok=True)
os.makedirs(abnormal_action_folder, exist_ok=True)

# Dictionary to store the classification results
action_classifications = {
    "ApplyEyeMakeup": "Normal",  # Example classification, replace with your own
    "HandstandPushups": "Abnormal",  # Example classification, replace with your own
    # Add other actions and their classifications
}

# Loop through each action folder in the source folder
for action_folder in os.listdir(source_folder):
    source_path = os.path.join(source_folder, action_folder)

    # Check if the action folder is classified as normal or abnormal
    classification = action_classifications.get(action_folder, None)

    if classification == "Normal":
        destination_path = os.path.join(normal_action_folder, action_folder)
        shutil.copytree(source_path, destination_path)
        print(f"Copied {action_folder} to Normal Action folder.")
    elif classification == "Abnormal":
        destination_path = os.path.join(abnormal_action_folder, action_folder)
        shutil.copytree(source_path, destination_path)
        print(f"Copied {action_folder} to Abnormal Action folder.")
    else:
        print(f"Ignoring {action_folder}.")

print("Copy process completed.")
