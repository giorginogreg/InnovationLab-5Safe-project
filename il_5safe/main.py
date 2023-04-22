from models.faster_rcnn import FasterRCNN
from models.yolo import YOLOv5s, YOLOv5l, YOLOv7
from models.retina_net import RetinaNet
import timeit
import torch
from utils.logs_utils.logger import logger

# Load an image to use for testing
image = torch.rand((3, 416, 416))

# Create instances of the different models
yolov5s = YOLOv5s()
yolov5l = YOLOv5l()
yolov7 = YOLOv7()
frcnn = FasterRCNN(backbone=None, num_classes=1)
retinanet = RetinaNet(backbone=None, num_classes=1)

# Measure the time taken to run inference for each model
yolov5s_time = timeit.timeit(lambda: yolov5s.forward(image), number=10)
yolov5l_time = timeit.timeit(lambda: yolov5l.forward(image), number=10)
yolov7_time = timeit.timeit(lambda: yolov7.forward(image), number=10)
frcnn_time = timeit.timeit(lambda: frcnn.forward([image]), number=10)
retinanet_time = timeit.timeit(lambda: retinanet.forward([image]), number=10)

logger.info(f"YOLOv5s: {yolov5s_time}")
logger.info(f"YOLOv5l: {yolov5l_time}")
logger.info(f"YOLOv7: {yolov7_time}")
logger.info(f"Faster R-CNN: {frcnn_time}")
logger.info(f"RetinaNet: {retinanet_time}")
