from PIL import Image
from ultralytics import YOLO
import cv2
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Define the root directory
root_dir = 'Dataset/UCF101_n_frames/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01'

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

            # Replace 'UCF101_n_frames' with 'UCF-yolo' in the full folder path
            new_folder_path = dirpath.replace('UCF101_n_frames', 'UCF-yolo')

            # Create the image output folder path if it doesn't exist
            image_output_path = os.path.join(new_folder_path, 'image_output')
            os.makedirs(image_output_path, exist_ok=True)

            # Create the text output folder path if it doesn't exist
            text_output_path = os.path.join(new_folder_path, 'text_output')
            os.makedirs(text_output_path, exist_ok=True)

            # Create the new image and bounding box file paths
            new_image_path = os.path.join(image_output_path, image_name + '.jpg')
            new_bbox_file_path = os.path.join(text_output_path, image_name + '.txt')

            
            
            # ...

            # Show the results
            for r in results:
                # Convert YOLO results to YOLO-compatible annotation
            yolo_annotations = []
                
                # Access raw predictions
                raw_predictions = r.pred[0].cpu().numpy()
                
                # Extract labels and boxes from raw predictions
                labels = raw_predictions[:, -1]
                boxes = raw_predictions[:, :-1]

                for label, box in zip(labels, boxes):
                    class_id = int(label)  # Extract class ID
                    confidence = r.conf[0].item()  # Extract confidence score

                    # YOLO format: <class_id> <center_x> <center_y> <width> <height>
                    x_center = (box[0] + box[2]) / 2.0 / r.orig_shape[1]
                    y_center = (box[1] + box[3]) / 2.0 / r.orig_shape[0]
                    width = (box[2] - box[0]) / r.orig_shape[1]
                    height = (box[3] - box[1]) / r.orig_shape[0]

                    yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height} {confidence}")

                # Save YOLO-compatible annotations to the bounding box file
                with open(new_bbox_file_path, 'w') as f:
                    f.write('\n'.join(yolo_annotations))

                # Save the image
                im_array = r.plot()  # plot a BGR numpy array of predictions
                im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
                im.save(new_image_path)

            # ...




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
            image = cv2.putText(image, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Save the image
            cv2.imwrite(new_image_path, image)
