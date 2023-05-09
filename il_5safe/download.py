from torch import hub

yolov5_models = ["yolov5s", "yolov5m", "yolov5l", "yolov5x"]
yolov5s, yolov5m, yolov5l, yolov5x = [
    hub.load("ultralytics/yolov5", model, pretrained=True, force_reload=True)
    for model in yolov5_models
]
