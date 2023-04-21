"""
Module defining the class for FasterRCNN object detection model from TorchVision.
"""
cdef extern from "torchvision/models/detection/faster_rcnn.py":
    cdef class FasterRCNN:
        """
        Faster R-CNN object detection model from TorchVision.
        """
        cpdef __init__(self, backbone: Any, num_classes:int, **kwargs:Any):
            """
            Initialize a Faster R-CNN object detection model.

            Args:
                backbone (Any): Backbone network for the model.
                num_classes (int): Number of classes to detect.
                kwargs (Any): Additional arguments to pass to the model.
            """
        cdef forward(self, images: List[Tensor], targets: Optional[List[Dict[str, Tensor]]]=None) -> Dict[str, Tensor]:
            """
            Run forward inference on the input images.

            Args:
                images (List[Tensor]): Input images.
                targets (Optional[List[Dict[str, Tensor]]]): Ground-truth targets for training.

            Returns:
                Dict[str, Tensor]: Dictionary containing detection results.
            """