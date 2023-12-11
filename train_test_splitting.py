"""
1- output format for yolo training

train_dir = /workspaces/video-dataset-preprocess/train-data
^has results

data splitted in 3 folders:
train_dir/train
train_dir/test
train_dir/val

each folder:
./images
./labels

./images takes the images from UCF-preprocessed
./labels takes the labels from UCF_obj_detected

hierarchy of UCF-preprocessed:
./action_name/video_name/images.jpg

hierarchy of UCF_obj_detected:
./action_name/video_name/predict/labels/label.txt


70% training
15% testing
15% validation

"""

import os
import random
import shutil
import os
import shutil
# Define the paths
train_dir = "/workspaces/video-dataset-preprocess/train-data-sample"
ucf_preprocessed_dir_img = "/workspaces/video-dataset-preprocess/Dataset/UCF-preprocessed-sample"
ucf_obj_detected_dir_label = "/workspaces/video-dataset-preprocess/Dataset/UCF_obj_detected_sample"

# Create train, test, and validation directories
train_data_dir = os.path.join(train_dir, "train")
test_data_dir = os.path.join(train_dir, "test")
val_data_dir = os.path.join(train_dir, "val")

os.makedirs(train_data_dir, exist_ok=True)
os.makedirs(test_data_dir, exist_ok=True)
os.makedirs(val_data_dir, exist_ok=True)

#%%
#####################################################
# images

# Get the list of action names
action_names = os.listdir(ucf_preprocessed_dir_img)

# Iterate over each action name
for action_name in action_names:
    action_dir = os.path.join(ucf_preprocessed_dir_img, action_name)
    video_names = os.listdir(action_dir)

    # Iterate over each video name
    for video_name in video_names:
        video_dir = os.path.join(action_dir, video_name)
        image_files = os.listdir(video_dir)

        # Randomly shuffle the image files
        random.shuffle(image_files)

        # Calculate the number of images for each split
        num_images = len(image_files)
        num_train = int(0.7 * num_images)
        num_test = int(0.15 * num_images)
        num_val = num_images - num_train - num_test

        # Split the image files into train, test, and validation sets
        train_files = image_files[:num_train]
        test_files = image_files[num_train:num_train + num_test]
        val_files = image_files[num_train + num_test:]

        # Create the action directory in train, test, and validation directories
        train_action_dir = os.path.join(train_data_dir, action_name, "images")
        test_action_dir = os.path.join(test_data_dir, action_name, "images")
        val_action_dir = os.path.join(val_data_dir, action_name, "images")

        os.makedirs(train_action_dir, exist_ok=True)
        os.makedirs(test_action_dir, exist_ok=True)
        os.makedirs(val_action_dir, exist_ok=True)

        # Copy the image files to the respective directories
        for file in train_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(train_action_dir, file)
            shutil.copy(src, dst)

        for file in test_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(test_action_dir, file)
            shutil.copy(src, dst)

        for file in val_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(val_action_dir, file)
            shutil.copy(src, dst)


#%%
#####################################################
# labels

# Assign actions to labels
train_label_dir = os.path.join(train_dir, "train")
test_label_dir = os.path.join(train_dir, "test")
val_label_dir = os.path.join(train_dir, "val")

os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

for action_name in action_names:
    action_label_dir = os.path.join(ucf_obj_detected_dir_label, action_name)
    video_names = os.listdir(action_label_dir)

    # Iterate over each video name
    for video_name in video_names:
        labels_dir = os.path.join(action_label_dir, video_name, "predict", "labels")
        label_files = os.listdir(labels_dir)

        # Split the label files into train, test, and validation sets
        train_files = label_files[:num_train]
        test_files = label_files[num_train:num_train + num_test]
        val_files = label_files[num_train + num_test:]

        # Create the action directory in train, test, and validation directories
        train_action_dir = os.path.join(train_label_dir, action_name, "labels")
        test_action_dir = os.path.join(test_label_dir, action_name, "labels")
        val_action_dir = os.path.join(val_label_dir, action_name, "labels")

        os.makedirs(train_action_dir, exist_ok=True)
        os.makedirs(test_action_dir, exist_ok=True)
        os.makedirs(val_action_dir, exist_ok=True)

        # Copy the label files to the respective directories
        for file in train_files:
            src = os.path.join(labels_dir, file)
            dst = os.path.join(train_action_dir, file)
            shutil.copy(src, dst)

        for file in test_files:
            src = os.path.join(labels_dir, file)
            dst = os.path.join(test_action_dir, file)
            shutil.copy(src, dst)

        for file in val_files:
            src = os.path.join(labels_dir, file)
            dst = os.path.join(val_action_dir, file)
            shutil.copy(src, dst)

# Print the success message
print("Train-test splitting and label assignment completed successfully!")


# Print the success message
print("Train-test splitting completed successfully!")


#%%

#to assign actions to labels

# train = "/workspaces/video-dataset-preprocess/train-data/train"
# test = "/workspaces/video-dataset-preprocess/train-data/test"
# val = "/workspaces/video-dataset-preprocess/train-data/val"

# os.makedirs(train, exist_ok=True)
# os.makedirs(test, exist_ok=True)
# os.makedirs(val, exist_ok=True)
"""
# Keypoints
kpt_shape: [17, 3]  # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
# flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Classes
# names:
#   0: person
# # -----------------OR------------

names = {
    0: "ApplyEyeMakeup",
    1: "ApplyLipstick",
    2: "Archery",
    3: "BabyCrawling",
    4: "BalanceBeam",
    5: "BandMarching",
    6: "BaseballPitch",
    7: "Basketball",
    8: "BasketballDunk",
    9: "BenchPress",
    10: "Biking",
    11: "Billiards",
    12: "BlowDryHair",
    13: "BlowingCandles",
    14: "BodyWeightSquats",
    15: "Bowling",
    16: "BoxingPunchingBag",
    17: "BoxingSpeedBag",
    18: "BreastStroke",
    19: "BrushingTeeth",
    20: "CleanAndJerk",
    21: "CliffDiving",
    22: "CricketBowling",
    23: "CricketShot",
    24: "CuttingInKitchen",
    25: "Diving",
    26: "Drumming",
    27: "Fencing",
    28: "FieldHockeyPenalty",
    29: "FloorGymnastics",
    30: "FrisbeeCatch",
    31: "FrontCrawl",
    32: "GolfSwing",
    33: "Haircut",
    34: "HammerThrow",
    35: "Hammering",
    36: "HandstandPushups",
    37: "HandstandWalking",
    38: "HeadMassage",
    39: "HighJump",
    40: "HorseRace",
    41: "HorseRiding",
    42: "HulaHoop",
    43: "IceDancing",
    44: "JavelinThrow",
    45: "JugglingBalls",
    46: "JumpRope",
    47: "JumpingJack",
    48: "Kayaking",
    49: "Knitting",
    50: "LongJump",
    51: "Lunges",
    52: "MilitaryParade",
    53: "Mixing",
    54: "MoppingFloor",
    55: "Nunchucks",
    56: "ParallelBars",
    57: "PizzaTossing",
    58: "PlayingCello",
    59: "PlayingDaf",
    60: "PlayingDhol",
    61: "PlayingFlute",
    62: "PlayingGuitar",
    63: "PlayingPiano",
    64: "PlayingSitar",
    65: "PlayingTabla",
    66: "PlayingViolin",
    67: "PoleVault",
    68: "PommelHorse",
    69: "PullUps",
    70: "Punch",
    71: "PushUps",
    72: "Rafting",
    73: "RockClimbingIndoor",
    74: "RopeClimbing",
    75: "Rowing",
    76: "SalsaSpin",
    77: "ShavingBeard",
    78: "Shotput",
    79: "SkateBoarding",
    80: "Skiing",
    81: "Skijet",
    82: "SkyDiving",
    83: "SoccerJuggling",
    84: "SoccerPenalty",
    85: "StillRings",
    86: "SumoWrestling",
    87: "Surfing",
    88: "Swing",
    89: "TableTennisShot",
    90: "TaiChi",
    91: "TennisSwing",
    92: "ThrowDiscus",
    93: "TrampolineJumping",
    94: "Typing",
    95: "UnevenBars",
    96: "VolleyballSpiking",
    97: "WalkingWithDog",
    98: "WallPushups",
    99: "WritingOnBoard",
    100: "YoYo"
}

# overwrite classes in labels with class corresponding to action_name

# Calculate the ROI for a set of bounding boxes
def calculate_roi(bboxes):
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    # Find the minimum and maximum coordinates
    for bbox in bboxes:
        x, y, w, h = bbox
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x + w)
        max_y = max(max_y, y + h)

    # Calculate the ROI coordinates
    roi_x = min_x
    roi_y = min_y
    roi_w = max_x - min_x
    roi_h = max_y - min_y

    return roi_x, roi_y, roi_w, roi_h

# Add padding to a set of bounding boxes
def add_padding(bboxes, padding_percent):
    padded_bboxes = []

    # Calculate the padding values
    padding_x = padding_percent * bboxes[0][2]
    padding_y = padding_percent * bboxes[0][3]

    # Add padding to each bounding box
    for bbox in bboxes:
        x, y, w, h = bbox
        padded_x = x - padding_x
        padded_y = y - padding_y
        padded_w = w + 2 * padding_x
        padded_h = h + 2 * padding_y
        padded_bboxes.append((padded_x, padded_y, padded_w, padded_h))

    return padded_bboxes

# Assign actions to labels
def assign_actions_to_labels(action_names, label_dir):
    # Get the list of label files
    label_files = os.listdir(label_dir)

    # Iterate over each label file
    for label_file in label_files:
        label_path = os.path.join(label_dir, label_file)

        # Read the contents of the label file
        with open(label_path, 'r') as f:
            lines = f.readlines()

        # Iterate over each line in the label file
        for i, line in enumerate(lines):
            # Split the line by whitespace
            parts = line.split()

            # Get the class ID from the line
            class_id = int(parts[0])

            # Get the action name corresponding to the class ID
            action_name = action_names[class_id]

            # Update the class ID in the line
            parts[0] = str(action_name)

            # Join the parts back into a line
            updated_line = ' '.join(parts)

            # Replace the line in the label file
            lines[i] = updated_line

        # Write the updated lines back to the label file
        with open(label_path, 'w') as f:
            f.writelines(lines)

# # Define the paths
# train_dir = "/workspaces/video-dataset-preprocess/train-data"
# train_data_dir = os.path.join(train_dir, "train")
# test_data_dir = os.path.join(train_dir, "test")
# val_data_dir = os.path.join(train_dir, "val")

# Assign actions to labels in train directory
assign_actions_to_labels(action_names, train_data_dir)

# Assign actions to labels in test directory
assign_actions_to_labels(action_names, test_data_dir)

# Assign actions to labels in validation directory
assign_actions_to_labels(action_names, val_data_dir)

# Print the success message
print("Actions assigned to labels successfully!")

"""