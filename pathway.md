# STEPS

1. First we convert UCF101 dataset to nframes, basically extracting frames from each video (at 1 fps)
  - /utils/avi2jpg-Final.py

2. Then we write n-frames data for each video folder
   - /utils/n_frames_ucf101-Final.py
   and now we have completed Data Loading and have UCF101_n_frames

3. Next we need to apply some basic preprocessing steps on it
   - /dataloaders/ucf_dataset_persistent-Final.py
   we have passed it file containing names of all videos rather than one file from ucfTrainTestList we get UCF-preprocessed 

4. Next we apply ROI techiniques on it we apply a pretrained yolo model to detect people in the dataset and draw the bounding boxes
   - /model-predict-Final.py
   bboxes are stored in UCF_obj_detected

5. Next we need to alter the generated labels so they represent actions instead of objects we are also combining the bboxes and adding padding
   - /action_labelling_roi.py

# TODO
[multi line testing] 
we get updated labels in UCF_action_labelled_roi

6. Next we need to split the datasets into train test and val
   - /train_test_splitting_final.py
   it takes labels from "UCF_action_labelled_roi" and images from "UCF-preprocessed" it splits them
 - 70% train
 - 15% test
 - 15% validation
now we have our training data in /train-data

7. Next we will train a custom yolo model on the training data
   - /train-data/model-train.py
   we will have our best.pt model in /train-data/runs

# Thats it! we have our custom trained model
