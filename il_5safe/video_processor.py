import os
import cv2
import numpy as np
from logs_utils.logger import logger
import pandas as pd
from typing import Any


def process_video(
    video_path: str, yolov5: Any, output_data_directory: str
) -> None:
    """
    Process the video by performing object detection using YOLOv5 and saving the filtered results.

    Args:
        video_path (str): Path to the video file.
        yolov5 (Any): YOLOv5 model for object detection.
        output_data_directory (str): Directory to save the filtered results.

    Returns:
        None
    """
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    if not os.path.exists(output_data_directory):
        os.makedirs(output_data_directory)

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_count += 1
        logger.info(f"Processing frame {frame_count}...")

        results = yolov5(frame)

        # Filter the detections to include only bikes and pedestrians
        filtered_results = results.pandas().xyxy[0]
        filtered_results: pd.DataFrame = filtered_results[
            (filtered_results["class"] == "bicycle")
            | (filtered_results["class"] == "person")
        ]
        np.save(
            f"{output_data_directory}/frame_{frame_count}",
            filtered_results.to_numpy(),
        )
        results.save()

    video_capture.release()
