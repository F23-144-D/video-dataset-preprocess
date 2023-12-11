######converting results to xyxy
import os

# Convert all files in the "labels" folder
root_dir = 'runs/pose/predict' + '2'
labels_folder = root_dir + '/labels'
output_folder = root_dir + '/labels_xyxy'

def convert_yolo_to_xyxy(yolo_path, xyxy_path):
    with open(yolo_path, 'r') as yolo_file:
        lines = yolo_file.readlines()

    with open(xyxy_path, 'w') as xyxy_file:
        for line in lines:
            data = line.strip().split()
            class_id = int(data[0])
            center_x, center_y, width, height = map(float, data[1:5])

            # Calculate xyxy coordinates
            x1 = int((center_x - width / 2) * 1000)
            y1 = int((center_y - height / 2) * 1000)
            x2 = int((center_x + width / 2) * 1000)
            y2 = int((center_y + height / 2) * 1000)

            xyxy_file.write(f"{class_id} {x1} {y1} {x2} {y2}\n")


os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(labels_folder):
    if filename.endswith('.txt'):
        yolo_path = os.path.join(labels_folder, filename)
        xyxy_path = os.path.join(output_folder, filename.replace('.txt', '_xyxy.txt'))

        convert_yolo_to_xyxy(yolo_path, xyxy_path)

print("Conversion completed.")