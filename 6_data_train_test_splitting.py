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
root_dir = "./Dataset"
train_dir = root_dir + "/train-data"
ucf_action_labelled_roi_dir_label = root_dir + "/UCF_action_labelled_roi"
ucf_preprocessed_dir_img = root_dir + "/UCF-preprocessed"

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

print("###################################### IMAGE SPLITTING ######################################")

# Iterate over each action name
for action_name in action_names:
    action_dir = os.path.join(ucf_preprocessed_dir_img, action_name)
    # label_dir = os.path.join(ucf_action_labelled_roi_dir_label, action_name)
    
    video_names = os.listdir(action_dir)

    # Iterate over each video name
    for video_name in video_names:
        video_dir = os.path.join(action_dir, video_name)
        # label_video_dir = os.path.join(label_dir, video_name, "predict", "labels")
        
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
        
        #make label dirs
        train_label_dir = os.path.join(train_data_dir, "labels")
        test_label_dir = os.path.join(test_data_dir, "labels")
        val_label_dir = os.path.join(val_data_dir, "labels")
        
        os.makedirs(train_label_dir, exist_ok=True)
        os.makedirs(test_label_dir, exist_ok=True)
        os.makedirs(val_label_dir, exist_ok=True)

        # Copy the image files to the respective directories
        print()
        print("-----------------------------------Copying in train")
        for file in train_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(train_action_dir, f"{video_name}_{file}") #to prevent same name files overwriting
            
            #string manip for label
            # src -- root_dir/ucf_preprocessed_dir_img/action_name/video_name/{image_name}.jpg
            # src_label -- root_dir/ucf_action_labelled_roi_dir_label/action_name/video_name/predict/labels/{image_name}.txt
            
            # dst -- root_dir/train_dir/train/images/{video_name}+{image_name}.jpg
            # dst_label -- root_dir/train_dir/train/labels/{video_name}+{image_name}.txt
            
            #manip on src
            src_label = src.replace(f"{ucf_preprocessed_dir_img}", f"{ucf_action_labelled_roi_dir_label}")
            src_label = src_label.replace("image", "predict/labels/image")
            src_label = src_label.replace(".jpg", ".txt")
            
            #manip on dst
            dst_label = dst.replace("images", "labels")
            dst_label = dst_label.replace(".jpg", ".txt")
            
            shutil.copy(src, dst)
            shutil.copy(src_label, dst_label)
            print(f"Copying IMAGE {src} to {dst}")
            print(f"Copying LABEL {src_label} to {dst_label}")
            

        print()
        print("-----------------------------------Copying in test")
        for file in test_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(test_action_dir, f"{video_name}_{file}")
            
            #manip on src
            src_label = src.replace(f"{ucf_preprocessed_dir_img}", f"{ucf_action_labelled_roi_dir_label}")
            src_label = src_label.replace("image", "predict/labels/image")
            src_label = src_label.replace(".jpg", ".txt")
            
            #manip on dst
            dst_label = dst.replace("images", "labels")
            dst_label = dst_label.replace(".jpg", ".txt")
            
            shutil.copy(src, dst)
            shutil.copy(src_label, dst_label)
            print(f"Copying IMAGE {src} to {dst}")
            print(f"Copying LABEL {src_label} to {dst_label}")
        
        print()
        print("-----------------------------------Copying in val")
        for file in val_files:
            src = os.path.join(video_dir, file)
            dst = os.path.join(val_action_dir, f"{video_name}_{file}")
            
            #manip on src
            src_label = src.replace(f"{ucf_preprocessed_dir_img}", f"{ucf_action_labelled_roi_dir_label}")
            src_label = src_label.replace("image", "predict/labels/image")
            src_label = src_label.replace(".jpg", ".txt")
            
            #manip on dst
            dst_label = dst.replace("images", "labels")
            dst_label = dst_label.replace(".jpg", ".txt")
            
            shutil.copy(src, dst)
            shutil.copy(src_label, dst_label)
            print(f"Copying IMAGE {src} to {dst}")
            print(f"Copying LABEL {src_label} to {dst_label}")


#%%
#####################################################
# # labels

# # Assign actions to labels
# train_label_dir = os.path.join(train_dir, "train")
# test_label_dir = os.path.join(train_dir, "test")
# val_label_dir = os.path.join(train_dir, "val")

# os.makedirs(train_label_dir, exist_ok=True)
# os.makedirs(test_label_dir, exist_ok=True)
# os.makedirs(val_label_dir, exist_ok=True)

# print()
# print()
# print()
# print("###################################### LABEL SPLITTING ######################################")

# for action_name in action_names:
#     action_label_dir = os.path.join(ucf_action_labelled_roi_dir_label, action_name)
#     video_names = os.listdir(action_label_dir)

#     # Iterate over each video name
#     for video_name in video_names:
#         labels_dir = os.path.join(action_label_dir, video_name, "predict", "labels")
#         label_files = os.listdir(labels_dir)

#         # Split the label files into train, test, and validation sets
#         train_files = label_files[:num_train]
#         test_files = label_files[num_train:num_train + num_test]
#         val_files = label_files[num_train + num_test:]

#         # Create the action directory in train, test, and validation directories
#         train_action_dir = os.path.join(train_label_dir, "labels")
#         test_action_dir = os.path.join(test_label_dir, "labels")
#         val_action_dir = os.path.join(val_label_dir, "labels")

#         os.makedirs(train_action_dir, exist_ok=True)
#         os.makedirs(test_action_dir, exist_ok=True)
#         os.makedirs(val_action_dir, exist_ok=True)

#         # Copy the label files to the respective directories
#         print()
#         print("-----------------------------------Copying labels in train")
#         for file in train_files:
#             src = os.path.join(labels_dir, file)
#             dst = os.path.join(train_action_dir, f"{video_name}_{file}")
#             shutil.copy(src, dst)

#         print()
#         print("-----------------------------------Copying labels in test")
#         for file in test_files:
#             src = os.path.join(labels_dir, file)
#             dst = os.path.join(test_action_dir, f"{video_name}_{file}")
#             shutil.copy(src, dst)

#         print()
#         print("-----------------------------------Copying labels in val")
#         for file in val_files:
#             src = os.path.join(labels_dir, file)
#             dst = os.path.join(val_action_dir, f"{video_name}_{file}")
#             shutil.copy(src, dst)
