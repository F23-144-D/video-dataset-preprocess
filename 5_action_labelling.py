import os
"""
has to be run BEFORE train-test-val splitting
because in the splitting, action association is lost
"""

#either ROI or pose estimation
APPLY_ROI = False

# Define the directory paths
root_dir = "./Dataset"
input_dir = root_dir + "/UCF_obj_detected"
output_dir = root_dir + "/UCF_action_labelled_roi"

#%% functions

actions = {
    "ApplyEyeMakeup": 0,
    "ApplyLipstick": 1,
    "Archery": 2,
    "BabyCrawling": 3,
    "BalanceBeam": 4,
    "BandMarching": 5,
    "BaseballPitch": 6,
    "Basketball": 7,
    "BasketballDunk": 8,
    "BenchPress": 9,
    "Biking": 10,
    "Billiards": 11,
    "BlowDryHair": 12,
    "BlowingCandles": 13,
    "BodyWeightSquats": 14,
    "Bowling": 15,
    "BoxingPunchingBag": 16,
    "BoxingSpeedBag": 17,
    "BreastStroke": 18,
    "BrushingTeeth": 19,
    "CleanAndJerk": 20,
    "CliffDiving": 21,
    "CricketBowling": 22,
    "CricketShot": 23,
    "CuttingInKitchen": 24,
    "Diving": 25,
    "Drumming": 26,
    "Fencing": 27,
    "FieldHockeyPenalty": 28,
    "FloorGymnastics": 29,
    "FrisbeeCatch": 30,
    "FrontCrawl": 31,
    "GolfSwing": 32,
    "Haircut": 33,
    "HammerThrow": 34,
    "Hammering": 35,
    "HandstandPushups": 36,
    "HandstandWalking": 37,
    "HeadMassage": 38,
    "HighJump": 39,
    "HorseRace": 40,
    "HorseRiding": 41,
    "HulaHoop": 42,
    "IceDancing": 43,
    "JavelinThrow": 44,
    "JugglingBalls": 45,
    "JumpRope": 46,
    "JumpingJack": 47,
    "Kayaking": 48,
    "Knitting": 49,
    "LongJump": 50,
    "Lunges": 51,
    "MilitaryParade": 52,
    "Mixing": 53,
    "MoppingFloor": 54,
    "Nunchucks": 55,
    "ParallelBars": 56,
    "PizzaTossing": 57,
    "PlayingCello": 58,
    "PlayingDaf": 59,
    "PlayingDhol": 60,
    "PlayingFlute": 61,
    "PlayingGuitar": 62,
    "PlayingPiano": 63,
    "PlayingSitar": 64,
    "PlayingTabla": 65,
    "PlayingViolin": 66,
    "PoleVault": 67,
    "PommelHorse": 68,
    "PullUps": 69,
    "Punch": 70,
    "PushUps": 71,
    "Rafting": 72,
    "RockClimbingIndoor": 73,
    "RopeClimbing": 74,
    "Rowing": 75,
    "SalsaSpin": 76,
    "ShavingBeard": 77,
    "Shotput": 78,
    "SkateBoarding": 79,
    "Skiing": 80,
    "Skijet": 81,
    "SkyDiving": 82,
    "SoccerJuggling": 83,
    "SoccerPenalty": 84,
    "StillRings": 85,
    "SumoWrestling": 86,
    "Surfing": 87,
    "Swing": 88,
    "TableTennisShot": 89,
    "TaiChi": 90,
    "TennisSwing": 91,
    "ThrowDiscus": 92,
    "TrampolineJumping": 93,
    "Typing": 94,
    "UnevenBars": 95,
    "VolleyballSpiking": 96,
    "WalkingWithDog": 97,
    "WallPushups": 98,
    "WritingOnBoard": 99,
    "YoYo": 100
}

#%%
"""
applied on Dataset/UCF_obj_detected
stores in Dataset/UCF_action_labelled

-- labels dir
../Dataset/UCF_obj_detected/{action_name}/{video_name}/predict/labels/{frame_name}.txt

take each of these labels, replace the first number (class id) with class from names[action_name]

"""

#%%

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over the action directories
for action_name in os.listdir(input_dir):
    action_dir = os.path.join(input_dir, action_name)
    if not os.path.isdir(action_dir):
        continue

    # Iterate over the video directories
    for video_name in os.listdir(action_dir):
        video_dir = os.path.join(action_dir, video_name)
        if not os.path.isdir(video_dir):
            continue

        print(f"Processing {video_name}...")
        print("########################################################################")

        # Iterate over the label files
        labels_dir = os.path.join(video_dir, "predict", "labels")
        for frame_name in os.listdir(labels_dir):
            label_file = os.path.join(labels_dir, frame_name)
            if not os.path.isfile(label_file):
                continue

            # Read the label file
            with open(label_file, "r") as f:
                lines = f.readlines()
                modlines = f.readlines()
                
            #empty mod lines
            for i in range(len(modlines)):
                modlines[i] = " "

            # Replace the class id with the action id
            action_id = actions[action_name]
            for i in range(len(lines)):
                class_id, *rest = lines[i].split()
<<<<<<<< Updated upstream:5_action_labelling.py
                lines[i] = f"{action_id} {' '.join(rest)}\n"  # Append newline character
========
                lines[i] = f"{action_id} {' '.join(rest)}"
>>>>>>>> Stashed changes:5_action_labelling_roi_processing.py
                print(f"Line {i} after action labelling: ", lines[i])
                
            print("-----------------------------------------------------------------------")

<<<<<<<< Updated upstream:5_action_labelling.py
========
            # bboxes = [(float(bbox.split()[1]), float(bbox.split()[2]), float(bbox.split()[3]), float(bbox.split()[4])) for bbox in lines]
            # # print("Original bboxes: ", bboxes)

            # if APPLY_ROI:
            #     roi_bboxes = calculate_roi(bboxes)
            #     padded_bboxes = add_padding(roi_bboxes)
            # else:
            #     padded_bboxes = add_padding(bboxes)
            
            # # print("Processed bboxes: ", padded_bboxes)

            # # Convert the padded bounding boxes back to lines
            # for i in range(len(lines)):
            #     _, bbox1, bbox2, bbox3, bbox4, *rest = lines[i].split()
            #     lines[i] = f"{action_id} {padded_bboxes[i][0]} {padded_bboxes[i][1]} {padded_bboxes[i][2]} {padded_bboxes[i][3]} {' '.join(rest)}"
            #     print(f"Line {i} after modding: ", lines[i])
            # # mod_lines = [f"{action_id} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n" for bbox in padded_bboxes]
            
>>>>>>>> Stashed changes:5_action_labelling_roi_processing.py
            print("#####################################################################")
            print("")
            print("")

            # Write the modified label file to the output directory
            output_subdir = os.path.join(output_dir, action_name, video_name, "predict", "labels")
            os.makedirs(output_subdir, exist_ok=True)
            output_file = os.path.join(output_subdir, frame_name)
            with open(output_file, "w") as f:
                f.writelines(lines)

