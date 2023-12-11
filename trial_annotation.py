# from PIL import Image
# from ultralytics import YOLO
# import cv2
# import os

# # Load a pretrained YOLOv8n model
# model = YOLO('yolov8n-pose.pt')

# # Define the root directory
# root_dir = 'Dataset/UCF101_n_frames/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01'

# # Walk through all files in the directory
# for dirpath, dirnames, filenames in os.walk(root_dir):
#     for filename in filenames:
#         # Only process .jpg files
#         if filename.endswith('.jpg'):
#             # Get the full path of the file
#             image_path = os.path.join(dirpath, filename)

#             # Run inference on the image
#             results = model(image_path)

#             # Get the image name without extension
#             image_name = os.path.splitext(filename)[0]

#             # Print the results on the console
#             print(f"Results for {image_name}:")
#             for r in results.xyxy[0]:
#                 print(f"Class: {r[5]}, Confidence: {r[4]}, Bounding Box: {r[:4]}")

#             # Normalize the path's separators and split the path into parts
#             path_parts = os.path.normpath(dirpath).split(os.sep)
#             print(path_parts)

#             # Find the index of the "UCF101_n_frames" part
#             index = path_parts.index('UCF101_n_frames') + 1

#             # Get the folder name after "UCF101_n_frames"
#             folder_name = path_parts[index]

#             # Print the folder name to the console
#             print("Action name: " + folder_name)

#             # Load the image
#             image = cv2.imread(image_path)

#             # Draw the action name on the image
#             text = "Action detected: " + folder_name
#             image = cv2.putText(image, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#             # Display the image
#             cv2.imshow("Result", image)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()











from PIL import Image
from ultralytics import YOLO
import cv2
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n-pose.pt')

# Define the root directory
root_dir = 'Dataset/UCF101_n_frames/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01'

# Create a list to store the results
all_results = []

# Walk through all files in the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # Only process .jpg files
        if filename.endswith('.jpg'):
            # Get the full path of the file
            image_path = os.path.join(dirpath, filename)

            # Run inference on the image
            results = model(image_path)

            # Get the desired values
            cls = int(results.cls.item())
            xywhn = results.xywhn[0].tolist()
            xyxyn = results.xyxyn[0].tolist()

            # Store the results in the desired format
            result_str = f"{cls} {' '.join(map(str, xywhn))} {' '.join(map(str, xyxyn))}"
            all_results.append(result_str)

            # ... (rest of your code remains unchanged)

# Save the results to a text file
output_file_path = 'output_results.txt'
with open(output_file_path, 'w') as output_file:
    for result_str in all_results:
        output_file.write(result_str + '\n')

print(f"Results saved to {output_file_path}")

