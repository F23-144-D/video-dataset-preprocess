from PIL import Image
from ultralytics import YOLO
import cv2
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Define the root directory
root_dir = 'Dataset/UCF101_n_frames'

# Walk through all files in the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # Only process .jpg files
        if filename.endswith('.jpg'):
            # Get the full path of the file
            image_path = os.path.join(dirpath, filename)

            # Run inference on the image
            results = model(image_path)

            # Get the image name without extension
            image_name = os.path.splitext(filename)[0]

            # Create the bounding box file name
            bbox_file_name = image_name + '.txt'

            # Replace 'UCF101_n_frames' with 'UCF-yolo' in the full folder path
            new_folder_path = dirpath.replace('UCF101_n_frames', 'UCF-yolo')

            # Create the new folder path if it doesn't exist
            os.makedirs(new_folder_path, exist_ok=True)

            # Create the new image and bounding box file paths
            new_image_path = os.path.join(new_folder_path, image_name + '.jpg')
            new_bbox_file_path = os.path.join(new_folder_path, bbox_file_name)

            # Show the results
            for r in results:
                im_array = r.plot()  # plot a BGR numpy array of predictions
                im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

                # Save the image and the bounding box file
                im.save(new_image_path)
                with open(new_bbox_file_path, 'w') as f:
                    f.write(str(r.boxes) + '\n')  # write the Boxes object containing the detection bounding boxes

          
            # Normalize the path's separators and split the path into parts
            path_parts = os.path.normpath(dirpath).split(os.sep)
            print(path_parts)

            # Find the index of the "UCF101_n_frames" part
            index = path_parts.index('UCF101_n_frames') + 1

            # Get the folder name after "UCF101_n_frames"
            folder_name = path_parts[index]

            # Print the folder name to the console
            print("Action name: " + folder_name)

            # Load the image
            image = cv2.imread(new_image_path)

            # Draw the action name on the image
            text = "Action detected: " + folder_name
            image = cv2.putText(image, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

            # Save the image
            cv2.imwrite(new_image_path, image)            