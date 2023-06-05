# Innovation Lab Project

### Files

    - auto_label.py: This file is responsible for processing the video by performing object detection using YOLOv5 and saving the filtered results as numpy arrays. The script takes the path to the video file as an environment variable, loads the YOLOv5 model, and processes each frame of the video. It filters the detected objects to include only bikes and pedestrians, and saves the filtered results as numpy arrays in a specified output directory.

    - process_video.py: This file contains the core logic for processing the video. It defines the process_video function, which takes the video path, YOLOv5 model, and output data directory as arguments. The function reads each frame of the video, performs object detection using the YOLOv5 model, filters the detected objects to include only bikes and pedestrians, and saves the filtered results as numpy arrays in the output data directory.
    the labeled images are saved then in `./run`

#### order_predictions.py
This file is responsible to order the rows in the predicted files obtained after the run of the script predict.py in the YoloV5 Model  
The rows in the files will be overwritten, and them will be sorted in the following order:
- first of all, they will be sorted by the first column (class)
- following, them will be sorted by the second parameter (x of the box detected)

This will be useful for comparing the boxes detected by the script (detect.py from yolo) and the annotation labels that we did manually

##### Usage: `poetry run python order_predictions.py [path] `  
where the [path] parameter will be the absolute path to the folder containing all the txt files to sort


---

## Prerequisites

Before running the scripts, make sure you have the following dependencies installed in the `requirements.txt`
or you can run `poetry install` to install them using `pypoetry`

## Usage

    - Ensure that the video file is available in the specified path or provide the correct path to the video file.
    - Adjust any configuration parameters as needed, such as the video file path, YOLOv5 model selection, and output data directory.
    - Run `auto_label.py` to process the video and save the filtered results as numpy arrays.
    - you can run also using `pypoetry`: `poetry run python il_5safe/auto_label.py`

