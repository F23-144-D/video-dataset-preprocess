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
# Define the paths
train_dir = "/workspaces/video-dataset-preprocess/train-data-sample"
ucf_action_labelled_roi_dir_img = "/workspaces/video-dataset-preprocess/Dataset/UCF_action_labelled_roi_sample"
ucf_obj_detected_dir_label = "/workspaces/video-dataset-preprocess/Dataset/UCF_obj_detected_sample"

# Create train, test, and validation directories
train_data_dir = os.path.join(train_dir, "train")
test_data_dir = os.path.join(train_dir, "test")
val_data_dir = os.path.join(train_dir, "val")

os.makedirs(train_data_dir, exist_ok=True)
os.makedirs(test_data_dir, exist_ok=True)
os.makedirs(val_data_dir, exist_ok=True)





#%% actions images
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
        train_action_dir = os.path.join(train_data_dir, "images")
        test_action_dir = os.path.join(test_data_dir, "images")
        val_action_dir = os.path.join(val_data_dir, "images")

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
        train_action_dir = os.path.join(train_label_dir, "labels")
        test_action_dir = os.path.join(test_label_dir, "labels")
        val_action_dir = os.path.join(val_label_dir, "labels")

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
print("Train-test-val splitting and label assignment completed successfully!")


# Print the success message
print("Train-test-val splitting completed successfully!")
