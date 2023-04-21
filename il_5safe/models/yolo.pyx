"""
Module defining classes for object YOLO detection models from TorchVision.
"""


cdef extern from "torchvision/models/detection/yolo.py":
    cdef class YOLOv5s:
        """
        YOLOv5s object detection model from TorchVision.
        """
        cpdef __init__(self, bool pretrained=True):
            """
            Initialize a YOLOv5s object detection model.

            Args:
                pretrained (bool): Whether to load the pretrained weights.
            """
        cpdef forward(self, Tensor x) -> List[Dict[str, Tensor]]:
            """
            Run forward inference on the input tensor.

            Args:
                x (Tensor): Input tensor.

            Returns:
                List[Dict[str, Tensor]]: List of dictionaries containing detection
                results for each input image.
            """

    cdef class YOLOv5l:
        """
        YOLOv5l object detection model from TorchVision.
        """
        cpdef __init__(self, bool pretrained=True):
            """
            Initialize a YOLOv5l object detection model.

            Args:
                pretrained (bool): Whether to load the pretrained weights.
            """
        cpdef forward(self, Tensor x) -> List[Dict[str, Tensor]]:
            """
            Run forward inference on the input tensor.

            Args:
                x (Tensor): Input tensor.

            Returns:
                List[Dict[str, Tensor]]: List of dictionaries containing detection
                results for each input image.
            """
    cdef class YOLOv7:
        """
        YOLOv7 object detection model from TorchVision.
        """
        cpdef __init__(self, bool pretrained=True):
            """
            Initialize a YOLOv7 object detection model.

            Args:
                pretrained (bool): Whether to load the pretrained weights.
            """
        cpdef forward(self, Tensor x) -> List[Dict[str, Tensor]]:
            """
            Run forward inference on the input tensor.

            Args:
                x (Tensor): Input tensor.

            Returns:
                List[Dict[str, Tensor]]: List of dictionaries containing detection
                results for each input image.
            """
