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
import shutil
import random

# Define the root directories
root_dir = "F:/GitHub/video-dataset-preprocess/"
ucf_obj_detected_dir = os.path.join(root_dir, "Dataset/UCF_action_labelled_roi")
ucf_preprocessed_dir = os.path.join(root_dir, "Dataset/UCF-preprocessed")

# Define the destination directories
train_dir = os.path.join(root_dir, "train-data/train")
test_data_dir = os.path.join(root_dir, "train-data/test")
val_data_dir = os.path.join(root_dir, "train-data/val")

# Get the list of action names
action_names = os.listdir(ucf_preprocessed_dir)

# Iterate over each action name
for action_name in action_names:
    # Define the source directories for each dataset
    obj_detected_dir = os.path.join(ucf_obj_detected_dir, action_name)
    preprocessed_dir = os.path.join(ucf_preprocessed_dir, action_name)

    # Get the video names
    video_names = os.listdir(preprocessed_dir)

    # Iterate over each video name
    for video_name in video_names:
        # Define the source directories for each video
        detected_video_dir = os.path.join(obj_detected_dir, video_name, "predict/labels")
        preprocessed_video_dir = os.path.join(preprocessed_dir, video_name)

        # Get the list of image and label files
        image_files = os.listdir(preprocessed_video_dir)
        label_files = os.listdir(detected_video_dir)

        # Shuffle the files
        random.shuffle(image_files)
        random.shuffle(label_files)

        # Calculate the number of images for each split
        num_images = len(image_files)
        num_train = int(0.7 * num_images)
        num_test = int(0.15 * num_images)
        num_val = num_images - num_train - num_test

        # Split the image files into train, test, and validation sets
        train_images = image_files[:num_train]
        test_images = image_files[num_train:num_train + num_test]
        val_images = image_files[num_train + num_test:]

        # Split the label files into train, test, and validation sets
        train_labels = label_files[:num_train]
        test_labels = label_files[num_train:num_train + num_test]
        val_labels = label_files[num_train + num_test:]

        # Define the destination directories for images and labels
        train_img_dir = os.path.join(train_dir, "images")
        train_lbl_dir = os.path.join(train_dir, "labels")
        test_img_dir = os.path.join(test_data_dir, "images")
        test_lbl_dir = os.path.join(test_data_dir, "labels")
        val_img_dir = os.path.join(val_data_dir, "images")
        val_lbl_dir = os.path.join(val_data_dir, "labels")

        # Create the destination directories
        os.makedirs(train_img_dir, exist_ok=True)
        os.makedirs(train_lbl_dir, exist_ok=True)
        os.makedirs(test_img_dir, exist_ok=True)
        os.makedirs(test_lbl_dir, exist_ok=True)
        os.makedirs(val_img_dir, exist_ok=True)
        os.makedirs(val_lbl_dir, exist_ok=True)

        # Copy and rename the image files to the respective directories
        for file in train_images:
            _, image_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{image_name}"
            shutil.copy(os.path.join(preprocessed_video_dir, file), os.path.join(train_img_dir, new_name))

        for file in test_images:
            _, image_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{image_name}"
            shutil.copy(os.path.join(preprocessed_video_dir, file), os.path.join(test_img_dir, new_name))

        for file in val_images:
            _, image_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{image_name}"
            shutil.copy(os.path.join(preprocessed_video_dir, file), os.path.join(val_img_dir, new_name))

        # Create the destination directory for label files
        os.makedirs(train_lbl_dir, exist_ok=True)

        # Copy the label files to the respective directories
        for file in train_labels:
            _, label_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{label_name}"
            shutil.copy(os.path.join(detected_video_dir, file), os.path.join(train_lbl_dir, new_name))

        for file in test_labels:
            _, label_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{label_name}"
            shutil.copy(os.path.join(detected_video_dir, file), os.path.join(test_lbl_dir, new_name))

        for file in val_labels:
            _, label_name = os.path.split(file)
            new_name = f"{action_name}_{video_name}_{label_name}"
            shutil.copy(os.path.join(detected_video_dir, file), os.path.join(val_lbl_dir, new_name))
