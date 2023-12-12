"""
has to be run BEFORE train-test-val splitting
because in the splitting, action association is lost
"""


import os
import random
import shutil

#%%

def assign_action_to_label(label_file, file):
    ################## add classes to labels
    # Read the contents of the label file
    with open(os.path.join(label_file, file), 'r') as f:
        lines = f.readlines()

    # Iterate over each line in the label file
    for i, line in enumerate(lines):
        # Split the line by whitespace
        parts = line.split()

        # Get the class ID from the line
        class_id = int(parts[0])

        # Get the action name corresponding to the class ID
        action_name = names[class_id]

        # Update the class ID in the line
        parts[0] = str(action_name)

        # Join the parts back into a line
        updated_line = ' '.join(parts)

        # Replace the line in the label file
        lines[i] = updated_line

    # Write the updated lines back to the label file
    with open(os.path.join(label_file, file), 'w') as f:
        f.writelines(lines)



#%%


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

        ################## add classes to labels
        # Read the contents of the label file
        with open(os.path.join(val_action_dir, file), 'r') as f:
            lines = f.readlines()

        # Iterate over each line in the label file
        for i, line in enumerate(lines):
            # Split the line by whitespace
            parts = line.split()

            # Get the class ID from the line
            class_id = int(parts[0])

            # Get the action name corresponding to the class ID
            action_name = names[class_id]

            # Update the class ID in the line
            parts[0] = str(action_name)

            # Join the parts back into a line
            updated_line = ' '.join(parts)

            # Replace the line in the label file
            lines[i] = updated_line

        # Write the updated lines back to the label file
        with open(os.path.join(val_action_dir, file), 'w') as f:
            f.writelines(lines)

# Print the success message
print("Train-test-val splitting and label assignment completed successfully!")


# Print the success message
print("Train-test-val splitting completed successfully!")

#%%


# Keypoints
kpt_shape: [17, 3]  # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
# flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Classes
# names:
#   0: person
# # -----------------OR------------

# Assign actions to labels
def assign_actions_to_labels(action_names, label_dir, output_dir):


    # Get the list of label files
    label_files = os.listdir(label_dir)
    print(label_files, " label_files")

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

# train_dir = "/workspaces/video-dataset-preprocess/train-data-sample-classed"
# ucf_preprocessed_dir_img = "/workspaces/video-dataset-preprocess/Dataset/UCF-preprocessed-sample"
# ucf_obj_detected_dir_label = "/workspaces/video-dataset-preprocess/Dataset/UCF_obj_detected_sample"


# train_data_dir = os.path.join(train_dir, "train")
# test_data_dir = os.path.join(train_dir, "test")
# val_data_dir = os.path.join(train_dir, "val")

# os.makedirs(train_data_dir, exist_ok=True)
# os.makedirs(test_data_dir, exist_ok=True)
# os.makedirs(val_data_dir, exist_ok=True)


# # Get the list of action names
# action_names = os.listdir(ucf_preprocessed_dir_img)

# # Assign actions to labels in train directory
# assign_actions_to_labels(action_names, ucf_obj_detected_dir_label, train_data_dir)

# # Assign actions to labels in test directory
# assign_actions_to_labels(action_names, ucf_obj_detected_dir_label, test_data_dir)

# # Assign actions to labels in validation directory
# assign_actions_to_labels(action_names, ucf_obj_detected_dir_label, val_data_dir)

# # Print the success message
# print("Actions assigned to labels successfully!")

