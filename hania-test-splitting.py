



import os
import numpy as np
from sklearn.model_selection import train_test_split
import shutil

# Directory containing the UCF101_n_frames dataset
image_dataset_dir = './Dataset/UCF101_n_frames'
label_dataset_dir = './Dataset/UCF-yolo'

# Output directory
output_dir = './UCF-trial'

# Get a list of all image files
image_files = [os.path.join(dirpath, filename)
               for dirpath, dirnames, filenames in os.walk(image_dataset_dir)
               for filename in filenames if filename.endswith('.jpg')]

# Convert the list to a numpy array and sort it
image_files = np.array(sorted(image_files))

# Get a list of all label files
label_files = [os.path.join(dirpath, filename)
               for dirpath, dirnames, filenames in os.walk(label_dataset_dir)
               for filename in filenames if filename.endswith('.txt')]

# Convert the list to a numpy array and sort it
label_files = np.array(sorted(label_files))

# Split the data into training and test sets
train_image_files, test_val_image_files = train_test_split(image_files, test_size=0.3, random_state=42)
val_image_files, test_image_files = train_test_split(test_val_image_files, test_size=0.5, random_state=42)

# Split the label files accordinglyUCF_obj_detectedd# Get the corresponding label files
_obj_detectedsedtrain_label_files = [os.path.join(UCF_obj_detectedd', os.path.relpath(image_file, UCF-preprocesseds')).replace('.jpg', '.txt') for image_file in train_image_files]
val_label_files = [os.path.join('UCF-preprocessed', os.path.relpath(image_file, 'UCF101_n_frames')).replace('.jpg', '.txt') for image_file in val_image_files]
test_label_files = [os.path.join('UCF-preprocessed', os.path.relpath(image_file, 'UCF101_n_frames')).replace('.jpg', '.txt') for image_file in test_image_files]



# Create folders for Train, Test, and Val
for folder in ['train', 'test', 'val']:
    os.makedirs(os.path.join(output_dir, folder, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, folder, 'images'), exist_ok=True)

# ... (unchanged code)

def copy_files(image_list, label_list, folder_type):
    for image_file, label_file in zip(image_list, label_list):
        destination_image_folder = os.path.join(output_dir, folder_type, 'images')
        destination_label_folder = os.path.join(output_dir, folder_type, 'labels')
        
        os.makedirs(destination_image_folder, exist_ok=True)
        os.makedirs(destination_label_folder, exist_ok=True)
        
        folder_name = os.path.basename(os.path.dirname(image_file))
                # Add debug print statements
        print(f"Copying {image_file} to {destination_image_folder}")
        print(f"Copying {label_file} to {destination_label_folder}")

        # Change the destination names to include folder_name_ prefix
        destination_image = os.path.join(destination_image_folder, f"{folder_name}_{os.path.basename(image_file)}")
        destination_label = os.path.join(destination_label_folder, f"{folder_name}_{os.path.basename(label_file)}")
        
        try:
            shutil.copy(image_file, destination_image)
            shutil.copy(label_file, destination_label)
        except FileNotFoundError:
            print(f"File not found: {image_file} or {label_file}")

# ... (unchanged code)


# Copy files to Train folder
copy_files(train_image_files, train_label_files, 'train')

# Copy files to Val folder
copy_files(val_image_files, val_label_files, 'val')

# Copy files to Test folder
copy_files(test_image_files, test_label_files, 'test')

# Calculate the percentages
total_files = len(image_files)
test_percentage = len(test_image_files) / total_files * 100
val_percentage = len(val_image_files) / total_files * 100
train_percentage = len(train_image_files) / total_files * 100

# Print the percentages
print(f"Test set percentage: {test_percentage}%")
print(f"Validation set percentage: {val_percentage}%")
print(f"Training set percentage: {train_percentage}%")
