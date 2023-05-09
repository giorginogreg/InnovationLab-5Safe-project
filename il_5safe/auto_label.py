import torch
import torchvision.models as models
from torchvision.models.detection.faster_rcnn import FasterRCNN
from torchvision.models.detection.retinanet import RetinaNet
from torchvision.models.detection.backbone_utils import (
    resnet_fpn_backbone,
    BackboneWithFPN,
)
import cv2
from yolov5.models.experimental import attempt_load

# Create a resnet50 backbone with fpn
backbone = models.resnet50(pretrained=True)
backbone.out_channels = 256
return_layers = {"layer1": 1, "layer2": 2, "layer3": 3, "layer4": 4}
in_channels_list = [256, 512, 1024, 2048]
out_channels = 256
backbone_with_fpn = BackboneWithFPN(
    backbone, return_layers, in_channels_list, out_channels
)

# # Load the pre-trained weights
# state_dict = torch.hub.load_state_dict_from_url(
#     'https://download.pytorch.org/models/resnet50-19c8e357.pth',
#     progress=True
# )
# backbone.load_state_dict(state_dict)

# Create instances of the different models
frcnn = FasterRCNN(backbone=backbone, num_classes=1)
retinanet = RetinaNet(backbone=backbone, num_classes=1)


# Load YOLOv5 models
yolov5s = attempt_load("yolov5s.pt", map_location=torch.device("cpu"))
yolov5m = attempt_load("yolov5m.pt", map_location=torch.device("cpu"))
yolov5l = attempt_load("yolov5l.pt", map_location=torch.device("cpu"))
yolov5x = attempt_load("yolov5x.pt", map_location=torch.device("cpu"))

# Example usage
video_path = "../assets/FRONTAL_2023-04-27-11 28 55.avi"
output_video_path = "./out/labeled/video.mp4"

# Open the video file
video_capture = cv2.VideoCapture(video_path)
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video_capture.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(
    output_video_path, fourcc, fps, (frame_width, frame_height)
)

while video_capture.isOpened():
    # Read the current frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Perform label detection on the frame using YOLO5x
    results = yolov5x(frame)

    # Perform checks with FasterRCNN
    img_tensor = torchvision.transforms.ToTensor()(frame)
    img_tensor = img_tensor.unsqueeze(0)
    predictions = frcnn(img_tensor)
    # Perform your checks with the predictions

    # Perform checks with RetinaNet
    img_tensor = torchvision.transforms.ToTensor()(frame)
    img_tensor = img_tensor.unsqueeze(0)
    predictions = retinanet(img_tensor)
    # Perform your checks with the predictions

    # Add labels to the frame
    labeled_frame = results.render()  # Use the labeled frame from YOLO5x
    # Perform any additional processing or drawing on the labeled frame

    # Write the labeled frame to the output video
    video_writer.write(labeled_frame)

# Release resources
video_capture.release()
video_writer.release()
