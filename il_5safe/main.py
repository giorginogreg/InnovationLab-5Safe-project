import os
from train import train_faster_rcnn
from torchvision import datasets, transforms

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Dataset preparation
transform = transforms.Compose([
    transforms.Resize((480, 640)),
    transforms.ToTensor(),
])
train_dataset = datasets.CocoDetection(
    root="./resources/images/training/",
    annFile="./resources/annotations/training.json",
    transform=transform)


faster_rcnn_model = train_faster_rcnn(
    train_dataset, num_classes=2, num_epochs=50
)
