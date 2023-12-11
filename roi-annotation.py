import os
import cv2
import numpy as np
from datetime import datetime

# Function to compute the region of interest (ROI) from bounding boxes
def compute_roi(bboxes):
    # Get the minimum and maximum coordinates
    x1 = min(bboxes[:, 0])
    y1 = min(bboxes[:, 1])
    x2 = max(bboxes[:, 2])
    y2 = max(bboxes[:, 3])

    return x1, y1, x2, y2

# Input directory containing images and annotations
input_dir = '/workspaces/video-dataset-preprocess/runs/pose/eyemakeup_10181137/predict'

# Output directory for the new annotations
output_dir = 'path_to_output_directory'
os.makedirs(output_dir, exist_ok=True)

# Load the class mapping from the YAML file
class_mapping = {
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
    100: "YoYo",

}

# Function to get the action class from the folder name
def get_action_class(dirpath):
    # return dirpath.split(os.path.sep)[-1]
    return "ApplyEyeMakeup"

# Iterate through each image in the input directory
for image_name in os.listdir(input_dir):
    if image_name.endswith('.jpg'):
        # Load the image
        image_path = os.path.join(input_dir, image_name)
        image = cv2.imread(image_path)

        print(image_path, ".................is image path")

        # Load bounding box annotations (assuming a text file with one line per object)
        annotation_path = os.path.join(input_dir, 'labels', image_name.replace('.jpg', '.txt'))
        if os.path.exists(annotation_path):
            with open(annotation_path, 'r') as file:
                lines = file.readlines()
            
            # Parse bounding box coordinates from the annotation file
            bboxes = []
            for line in lines:
                values = line.strip().split()
                class_id = int(values[0])
                x_center, y_center, width, height = map(float, values[1:5])

                # Convert to absolute coordinates
                x1 = int((x_center - width / 2) * image.shape[1])
                y1 = int((y_center - height / 2) * image.shape[0])
                x2 = int((x_center + width / 2) * image.shape[1])
                y2 = int((y_center + height / 2) * image.shape[0])

                bboxes.append([x1, y1, x2, y2, class_id])

            # Compute the region of interest (ROI) for the bounding boxes
            roi_x1, roi_y1, roi_x2, roi_y2 = compute_roi(np.array(bboxes)[:, :4])

            # Get the action class from the folder name
            action_class = get_action_class(input_dir)

            # Get the corresponding class number
            class_number = [k for k, v in class_mapping.items() if v == action_class][0]

            # Create the new annotation line
            new_annotation = f"{class_number} {roi_x1} {roi_y1} {roi_x2} {roi_y2}\n"

            # Save the new annotation to the output directory
            output_annotation_path = os.path.join(output_dir, image_name.replace('.jpg', '_action.txt'))
            with open(output_annotation_path, 'a') as output_file:
                output_file.write(new_annotation)

print("Conversion completed.")
