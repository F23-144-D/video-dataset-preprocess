import os
from torchvision import transforms
import cv2

import sys
sys.path.append('/workspaces/video-dataset-preprocess/dataloaders')
from ucf_dataset_functions import *

import imghdr

transform = transforms.Compose([
    ClipSubstractMean(),
    RandomCrop(),
    CenterCrop(),
    RandomHorizontalFlip()
])


# Define the root directory
root_dir = '/workspaces/video-dataset-preprocess/Dataset/UCF101_n_frames'

# Walk through all files in the directory
i = 1
for dirpath, dirnames, filenames in os.walk(root_dir):
    i = i + 1
    if i == 10:
        break

    # Iterate over each file
    for filename in filenames:

        # Check if the file is an image
        if imghdr.what(os.path.join(dirpath, filename)) is not None:
    
            # Load the image
            image_path = os.path.join(dirpath, filename)
            image = cv2.imread(image_path)

            # Apply the transformations
            transformed_image = transform(image)
            # Convert the image to a supported depth (e.g., 8-bit unsigned integer)
            transformed_image = (transformed_image * 255).astype(np.uint8)

            # Convert the image to the correct format (e.g., BGR)
            transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)


            # Create the output directory for the current action
            output_dir = dirpath.replace(root_dir, "/workspaces/video-dataset-preprocess/Dataset/UCF_preprocessed")
            os.makedirs(output_dir, exist_ok=True)

            # Save the transformed image to the output directory
            output_filename = os.path.join(output_dir, filename)
            print(f"Saving image to {output_filename}")
            cv2.imwrite(output_filename, transformed_image)
            print("Image saved successfully")


    

