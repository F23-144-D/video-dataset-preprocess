#----------------------------------------MANUAL------------------------------

import os
import shutil

# Define the source folder containing all action folders
source_folder = '/Dataset/UCF-yolo'

# Define the destination folders for normal and abnormal actions
normal_action_folder = '/Dataset/NormalAction'
abnormal_action_folder = '/Dataset/AbnormalAction'

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





#-------------------------------------Feature Enginerring----------------------------
from ultralytics.engine import results
import torch

# Example results for Normal Action
normal_action_result = results.Boxes(
    cls=torch.tensor([0.]),
    conf=torch.tensor([0.8754]),
    data=torch.tensor([[79.0000, 0.0000, 320.0000, 240.0000, 0.8754, 0.0000]]),
    id=None,
    is_track=False,
    orig_shape=(240, 320),
    shape=torch.Size([1, 6]),
    xywh=torch.tensor([[199.5000, 120.0000, 241.0000, 240.0000]]),
    xywhn=torch.tensor([[0.6234, 0.5000, 0.7531, 1.0000]]),
    xyxy=torch.tensor([[79., 0., 320., 240.]]),
    xyxyn=torch.tensor([[0.2469, 0.0000, 1.0000, 1.0000]])
)

# Example results for Abnormal Action
abnormal_action_result = results.Boxes(
    cls=torch.tensor([0.]),
    conf=torch.tensor([0.8260]),
    data=torch.tensor([[35.0000, 71.0000, 206.0000, 240.0000, 0.8260, 0.0000]]),
    id=None,
    is_track=False,
    orig_shape=(240, 320),
    shape=torch.Size([1, 6]),
    xywh=torch.tensor([[120.5000, 155.5000, 171.0000, 169.0000]]),
    xywhn=torch.tensor([[0.3766, 0.6479, 0.5344, 0.7042]]),
    xyxy=torch.tensor([[35., 71., 206., 240.]]),
    xyxyn=torch.tensor([[0.1094, 0.2958, 0.6438, 1.0000]])
)

# Function to extract features
def extract_features(result):
    features = {
        'class_index': result.cls.item(),
        'confidence': result.conf.item(),
        'normalized_bbox': result.xywhn.squeeze().tolist(),
        'original_bbox': result.xyxy.squeeze().tolist(),
        # Add more features as needed
    }
    return features

# Extract features for Normal Action
normal_action_features = extract_features(normal_action_result)
print("Features for Normal Action:")
print(normal_action_features)

# Extract features for Abnormal Action
abnormal_action_features = extract_features(abnormal_action_result)
print("\nFeatures for Abnormal Action:")
print(abnormal_action_features)
