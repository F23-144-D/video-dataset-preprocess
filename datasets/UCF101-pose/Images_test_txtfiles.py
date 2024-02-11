import os

# Define the destination directory and the subdirectories
dest_dir = 'F:/GitHub/video-dataset-preprocess/datasets/UCF101-pose/images'
subdirs = ['train', 'val']

# Iterate over the subdirectories
for subdir in subdirs:
    # Define the subdirectory and the .txt file
    subdir_path = os.path.join(dest_dir, subdir)
    txt_file = os.path.join(dest_dir, f'{subdir}.txt')

    # Get the full paths of the images in the subdirectory
    image_paths = [os.path.join(subdir_path, file_name) for file_name in os.listdir(subdir_path) if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Write the image paths to the .txt file
    with open(txt_file, 'w') as f:
        for image_path in image_paths:
            f.write(image_path + '\n')