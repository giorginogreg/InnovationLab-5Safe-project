import os
from train import train_faster_rcnn, train_retinanet
from torchvision import datasets, transforms
from data_utils import CustomDataset
from torchvision import datasets, transforms

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Dataset preparation
train_dataset = datasets.CocoDetection(
    root='./resources/images/training/',
    annFile='./resources/annotations/training.json', 
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

#faster_rcnn_model = train_faster_rcnn(train_dataset, num_classes=2)
