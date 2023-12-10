def convert_to_yolo_format(input_path, output_path, image_size):
    with open(input_path, 'r') as input_file:
        lines = input_file.readlines()

    yolo_annotations = []

    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center, y_center, box_width, box_height = map(float, parts[1:5])

        # Convert to YOLO format
        x_center_yolo = x_center
        y_center_yolo = y_center
        width_yolo = box_width
        height_yolo = box_height

        # YOLO format: <class_id> <center_x> <center_y> <width> <height>
        yolo_annotations.append(f"{class_id} {x_center_yolo} {y_center_yolo} {width_yolo} {height_yolo}")

    # Save YOLO-compatible annotations to the bounding box file
    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join(yolo_annotations))

# Example usage
input_path = 'path_to_input_annotations.txt'  # Replace with the actual path to your input annotations file
output_path = 'path_to_output_yolo_annotations.txt'  # Replace with the desired output path
image_size = (320, 240)  # Replace with the actual size of your images

convert_to_yolo_format(input_path, output_path, image_size)
