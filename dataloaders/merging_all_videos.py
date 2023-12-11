import os

def get_video_paths(root_folder):
    video_paths = []

    # Walk through the root folder
    for foldername, subfolders, filenames in os.walk(root_folder):
        # Check if there are video files in the current folder
        video_files = [filename for filename in filenames if filename.endswith('.avi')]
        
        # If there are video files, add their paths to the list
        if video_files:
            relative_foldername = foldername.replace(root_folder, '').lstrip(os.sep)
            video_paths.extend([os.path.join(relative_foldername, video_file).replace(os.sep, '/') for video_file in video_files])

    return video_paths


def write_video_paths_to_file(video_paths, output_file):
    with open(output_file, 'w') as file:
        for video_path in video_paths:
            file.write(video_path + '\n')

# Example usage:
root_folder = './Dataset/UCF-101'
output_txt_file = './Dataset/ucfTrainTestlist/all_videos.txt'

video_paths = get_video_paths(root_folder)

# Print the video paths for debugging
print("Video Paths:")
print(video_paths)

# Write the resulting video paths to a text file
write_video_paths_to_file(video_paths, output_txt_file)

print("Video paths have been written to:", output_txt_file)
