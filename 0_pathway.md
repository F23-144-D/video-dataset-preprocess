first we convert UCF101 dataset to nframes, basically extracting frames from each video (at 1 fps)

```
1_frame_extraction.py
```

[UCF101] --> [UCF101_n_frames]
now [UCF101] has no dependancies

then we write n-frames data for each video folder

```
2_writing_frame_data.py
```

[UCF101_n_frames] <--->
still has depenedancies

now we have completed Data Loading and have UCF101_n_frames

next we need to apply some basic preprocessing steps on it

```
3_data_preprocessing.py
```

[UCF101_n_frames], [all_videos.txt], [classInd.txt] --> [UCF-preprocessed]
now [UCF101_n_frames] has no dependancies
we have passed it file containing names of all videos rather than one file from ucfTrainTestList
we get UCF-preprocessed

next we apply ROI techiniques on it
we apply a pretrained yolo model to detect people in the dataset and draw the bounding boxes

```
4_object_pose_detection.py
```

[UCF-preprocessed] --> [UCF_obj_detected]
[UCF-preprocessed] still has dependancies
bboxes are stored in UCF_obj_detected

next we need to alter the generated labels so they represent actions instead of objects
we are also combining the bboxes and adding padding

```
5_action_labelling_roi_preprocessing.py 
```

[UCF_obj_detected] --> [UCF_action_labelled_roi]
now [UCF_obj_detected] has no dependancies

# TODO

multi line testing

we get updated labels in UCF_action_labelled_roi

next we need to split the datasets into train test and val

```
6_data_train_test_splitting.py
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

```
7_action_detection_model_training.py
```

[train-data], [ucf101.yaml] --> [best.pt]
now [train-data] has no dependancies, but it does contain model insights
we will have our best.pt model in /train-data/runs

Thats it! we have our custom trained model
