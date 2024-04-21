

#paths
# data folder root
data_root = './Dataset/'
raw_data = data_root + 'UCF-101'
n_frames = data_root + 'UCF101_n_frames'
processed_data = data_root + 'UCF-preprocessed'

#----------------------------------1_frame_extraction.py
#frames per second to extract
FPS_RATE = 1

#----------------------------------2_writing_frame_data.py
video_list = "all_videos.txt"
class_list = "classInd.txt"

#frames per video
CLIP_LENGTH = 8