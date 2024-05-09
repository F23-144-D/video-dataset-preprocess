import os

actions = {
    0 : 0,  # ApplyEyeMakeup, NormalAction
    1 : 0,  # ApplyLipstick, NormalAction
    2 : 0,  # Archery, NormalAction
    3 : 0,  # BabyCrawling, NormalAction
    4 : 1,  # BalanceBeam, AbnormalAction
    5 : 0,  # BandMarching, NormalAction
    6 : 0,  # BaseballPitch, NormalAction
    7 : 0,  # Basketball, NormalAction
    8 : 0,  # BasketballDunk, NormalAction
    9 : 1,  # BenchPress, AbnormalAction
    10: 0,  # Biking, NormalAction
    11: 0,  # Billiards, NormalAction
    12: 0,  # BlowDryHair, NormalAction
    13: 0,  # BlowingCandles, NormalAction
    14: 0,  # BodyWeightSquats, NormalAction
    15: 1,  # Bowling, AbnormalAction
    16: 1,  # BoxingPunchingBag, AbnormalAction
    17: 1,  # BoxingSpeedBag, AbnormalAction
    18: 0,  # BreastStroke, NormalAction
    19: 0,  # BrushingTeeth, NormalAction
    20: 0,  # CleanAndJerk, NormalAction
    21: 0,  # CliffDiving, NormalAction
    22: 0,  # CricketBowling, NormalAction
    23: 0,  # CricketShot, NormalAction
    24: 1,  # CuttingInKitchen, AbnormalAction
    25: 0,  # Diving, NormalAction
    26: 1,  # Drumming, AbnormalAction
    27: 0,  # Fencing, NormalAction
    28: 0,  # FieldHockeyPenalty, NormalAction
    29: 1,  # FloorGymnastics, AbnormalAction
    30: 1,  # FrisbeeCatch, AbnormalAction
    31: 0,  # FrontCrawl, NormalAction
    32: 1,  # GolfSwing, AbnormalAction
    33: 0,  # Haircut, NormalAction
    34: 1,  # Hammering, AbnormalAction
    35: 1,  # HammerThrow, AbnormalAction
    36: 1,  # HandstandPushups, AbnormalAction
    37: 1,  # HandstandWalking, AbnormalAction
    38: 0,  # HeadMassage, NormalAction
    39: 0,  # HighJump, NormalAction
    40: 0,  # HorseRace, NormalAction
    41: 0,  # HorseRiding, NormalAction
    42: 0,  # HulaHoop, NormalAction
    43: 0,  # IceDancing, NormalAction
    44: 1,  # JavelinThrow, AbnormalAction
    45: 0,  # JugglingBalls, NormalAction
    46: 1,  # JumpingJack, AbnormalAction
    47: 0,  # JumpRope, NormalAction
    48: 0,  # Kayaking, NormalAction
    49: 0,  # Knitting, NormalAction
    50: 0,  # LongJump, NormalAction
    51: 0,  # Lunges, NormalAction
    52: 0,  # MilitaryParade, NormalAction
    53: 0,  # Mixing, NormalAction
    54: 0,  # MoppingFloor, NormalAction
    55: 0,  # Nunchucks, NormalAction
    56: 1,  # ParallelBars, AbnormalAction
    57: 0,  # PizzaTossing, NormalAction
    58: 0,  # PlayingCello, NormalAction
    59: 0,  # PlayingDaf, NormalAction
    60: 0,  # PlayingDhol, NormalAction
    61: 0,  # PlayingFlute, NormalAction
    62: 0,  # PlayingGuitar, NormalAction
    63: 0,  # PlayingPiano, NormalAction
    64: 0,  # PlayingSitar, NormalAction
    65: 0,  # PlayingTabla, NormalAction
    66: 0,  # PlayingViolin, NormalAction
    67: 1,  # PoleVault, AbnormalAction
    68: 1,  # PommelHorse, AbnormalAction
    69: 1,  # PullUps, AbnormalAction
    70: 1,  # Punch, AbnormalAction
    71: 1,  # PushUps, AbnormalAction
    72: 0,  # Rafting, NormalAction
    73: 1,  # RockClimbingIndoor, AbnormalAction
    74: 1,  # RopeClimbing, AbnormalAction
    75: 0,  # Rowing, NormalAction
    76: 0,  # SalsaSpin, NormalAction
    77: 0,  # ShavingBeard, NormalAction
    78: 0,  # Shotput, NormalAction
    79: 1,  # SkateBoarding, AbnormalAction
    80: 0,  # Skiing, NormalAction
    81: 0,  # Skijet, NormalAction
    82: 0,  # SkyDiving, NormalAction
    83: 1,  # SoccerJuggling, AbnormalAction
    84: 0,  # SoccerPenalty, NormalAction
    85: 0,  # StillRings, NormalAction
    86: 1,  # SumoWrestling, AbnormalAction
    87: 0,  # Surfing, NormalAction
    88: 0,  # Swing, NormalAction
    89: 0,  # TableTennisShot, NormalAction
    90: 0,  # TaiChi, NormalAction
    91: 1,  # TennisSwing, AbnormalAction
    92: 1,  # ThrowDiscus, AbnormalAction
    93: 1,  # TrampolineJumping, AbnormalAction
    94: 0,  # Typing, NormalAction
    95: 0,  # UnevenBars, NormalAction
    96: 0,  # VolleyballSpiking, NormalAction
    97: 0,  # WalkingWithDog, NormalAction
    98: 0,  # WallPushups, NormalAction
    99: 0,  # WritingOnBoard, NormalAction
    100: 0  # YoYo, NormalAction
}

root_dir = "./Dataset/train-data"
train = root_dir + "/train/labels"
test = root_dir + "/test/labels"
val = root_dir + "/val/labels"

print()
print("-----------------------Editing Labels for TRAIN")
for labelfile in os.listdir(train):
    labelpath = os.path.join(train, labelfile)
    print("editing labelfile: ", labelfile)
    if not os.path.isfile(labelpath):
        print("skip")
        continue

    # Read the label file
    with open(labelpath, "r") as f:
        lines = f.readlines()
        # print("lines in : ", labelpath, " are: ", lines)
        modlines = f.readlines()

    # Empty mod lines
    for i in range(len(modlines)):
        modlines[i] = " "

    # Replace the action id with the abnormality id
    for i in range(len(lines)):
        action_id, *rest = lines[i].split()
        abd_id = actions[int(action_id)]
        lines[i] = f"{abd_id} {' '.join(rest)}\n"  # Append newline character
        # print(f"Line {i} after abnormality labelling: ", lines[i])
        
    #write new lines into the open file
    with open(labelpath, "w") as f:
        f.writelines(lines)
        

print()
print("-----------------------Editing Labels for TEST")
for labelfile in os.listdir(test):
    labelpath = os.path.join(test, labelfile)
    print("editing labelfile: ", labelfile)
    if not os.path.isfile(labelpath):
        print("skip")
        continue

    # Read the label file
    with open(labelpath, "r") as f:
        lines = f.readlines()
        # print("lines in : ", labelpath, " are: ", lines)
        modlines = f.readlines()

    # Empty mod lines
    for i in range(len(modlines)):
        modlines[i] = " "

    # Replace the action id with the abnormality id
    for i in range(len(lines)):
        action_id, *rest = lines[i].split()
        abd_id = actions[int(action_id)]
        lines[i] = f"{abd_id} {' '.join(rest)}\n"  # Append newline character
        # print(f"Line {i} after abnormality labelling: ", lines[i])
        
    #write new lines into the open file
    with open(labelpath, "w") as f:
        f.writelines(lines)
      

print()
print("-----------------------Editing Labels for VAL")
for labelfile in os.listdir(test):
    labelpath = os.path.join(test, labelfile)
    print("editing labelfile: ", labelfile)
    if not os.path.isfile(labelpath):
        print("skip")
        continue

    # Read the label file
    with open(labelpath, "r") as f:
        lines = f.readlines()
        # print("lines in : ", labelpath, " are: ", lines)
        modlines = f.readlines()

    # Empty mod lines
    for i in range(len(modlines)):
        modlines[i] = " "

    # Replace the action id with the abnormality id
    for i in range(len(lines)):
        action_id, *rest = lines[i].split()
        abd_id = actions[int(action_id)]
        lines[i] = f"{abd_id} {' '.join(rest)}\n"  # Append newline character
        # print(f"Line {i} after abnormality labelling: ", lines[i])
        
    #write new lines into the open file
    with open(labelpath, "w") as f:
        f.writelines(lines)