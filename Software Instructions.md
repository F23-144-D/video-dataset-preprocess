# Step 1: Dataset Download

Download the UCF101 dataset from the below website

```
https://www.crcv.ucf.edu/data/UCF101.php
```

# Step 2: Conversion of Video to Images

Convert UCF101 video dataset to images

```
1. utils/avi2jpg-Final.py                                      ['Dataset/UCF101_n_frames']
```

[UCF101] --> [UCF101_n_frames]

# Step 3: Conversion of Videos into n-frames

Convert UCF101 dataset to nframes, basically extracting frames from each video (at 1 fps) and then then we write n-frames data for each video folder

```
2. utils/n_frames_ucf101-Final.py
```

[UCF101] --> [UCF101_n_frames]
now [UCF101] has no dependancies

then we write n-frames data for each video folder

[UCF101_n_frames] <--->
still has depenedancies

now we have completed Data Loading and have UCF101_n_frames

next we need to apply some basic preprocessing steps on it

# Step 4: Data Pre-processing

```
3. dataloaders/ucf_dataset_persistent-Final.py                  ['Dataset/UCF-preprocessed']
```

[UCF101_n_frames], [all_videos.txt], [classInd.txt] --> [UCF-preprocessed]
now [UCF101_n_frames] has no dependancies
we have passed it file containing names of all videos rather than one file from ucfTrainTestList
we get UCF-preprocessed

next we apply ROI techiniques on it
we apply a pretrained yolo model to detect people in the dataset and draw the bounding boxes

# Step 5: Merging all videos list

```
4. dataloaders/merging_all_videos-Final.py                      ['Dataset/ucfTrainTestlist/all_videos.txt']
```

['Dataset/ucfTrainTestlist/all_videos.txt']

# Step 6: Setup Environment

Install Ultralytics YOLO for the pose detection

```
pip install -U ultralytics
```

# Step 7: Object Pose Detection

```
5. model-predict-Final.py                                       ['Dataset/UCF_obj_detected']
```

[UCF-preprocessed] --> [UCF_obj_detected]
[UCF-preprocessed] still has dependancies
bboxes are stored in UCF_obj_detected

next we need to alter the generated labels so they represent actions instead of objects
we are also combining the bboxes and adding padding

# Step 8: Action Labelling & ROI Pre-processing

```
6. action_labelling_roi-Final.py                                 ['Dataset/UCF_action_labelled_roi']
```

[UCF_obj_detected] --> [UCF_action_labelled_roi]
now [UCF_obj_detected] has no dependancies

# TODO

multi line testing

we get updated labels in UCF_action_labelled_roi

next we need to split the datasets into train test and val

# Step 9: Splitting in Train, Val, Test Folders

```
7. train_test_splitting-Final.py
```

[UCF_action_labelled_roi], [UCF-preprocessed] --> [train-data]
now both datasets have no dependancies

it takes labels from "UCF_action_labelled_roi" and images from "UCF-preprocessed"
it splits them
70% train
15% test
15% validation

now we have our training data in /train-data

next we will train a custom yolo model on the training data

# Step 10: Model Training

```
8. train-data/model-train-Final.py
```

[train-data], [ucf101.yaml] --> [best.pt]
now [train-data] has no dependancies, but it does contain model insights
we will have our best.pt model in /train-data/runs

Thats it! we have our custom trained model
