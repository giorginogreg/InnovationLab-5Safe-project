import os
import torch
from logs_utils.logger import logger
from video_processor import process_video

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Set device to GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    yolov5x = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True, device=device)
    video_name = os.getenv("VIDEO_NAME", "video_1")
    video_extension = os.getenv("VIDEO_EXTENSION", ".avi")
    video_path = f"./resources/{video_name}{video_extension}"
    output_data_directory = f"./out/data/{video_name}"

    if not os.path.isfile(video_path):
        logger.error(f"Video file does not exist at path: {video_path}")
        return

    logger.info("Starting video processing...")
    process_video(video_path, yolov5x, output_data_directory)
    logger.info("Video processing completed.")

if __name__ == "__main__":
    main()
