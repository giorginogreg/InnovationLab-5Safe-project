import torch
from torch.utils.data import DataLoader
from torchvision import models
from torch.utils.tensorboard import SummaryWriter

def train_model(model, train_dataset, num_epochs=20, num_classes=2, log_dir="./logs"):
    train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    criterion = torch.nn.CrossEntropyLoss()

    # Learning rate scheduler
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

    # TensorBoard writer
    writer = SummaryWriter(log_dir=log_dir)

    # Initialize evaluation metrics
    evaluator = CocoEvaluator(train_dataset)

    best_epoch = -1
    best_map = -1

    for epoch in range(num_epochs):
        train_one_epoch(model, train_dataloader, optimizer, device, epoch, writer, num_epochs)
        evaluate(model, train_dataloader, device, evaluator, epoch, writer)
        lr_scheduler.step()

        # Save checkpoint
        if (epoch + 1) % 5 == 0:
            checkpoint_path = f"checkpoint_epoch_{epoch+1}.pth"
            torch.save(model.state_dict(), checkpoint_path)
            print(f"Saved checkpoint: {checkpoint_path}")

        # Check if current epoch has the best mAP
        if evaluator.coco_eval["bbox"].stats[0] > best_map:
            best_epoch = epoch + 1
            best_map = evaluator.coco_eval["bbox"].stats[0]

    print(f"Best epoch: {best_epoch}, Best mAP: {best_map}")

    writer.close()

    return model


def train_one_epoch(model, dataloader, optimizer, device, epoch, writer, num_epochs):
    model.train()
    epoch_loss = 0.0
    for images, targets in dataloader:
        images = images.to(device)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        optimizer.zero_grad()
        outputs = model(images, targets)
        loss = sum(loss for loss in outputs.values())
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss/len(dataloader):.4f}")

    # Log training loss to TensorBoard
    writer.add_scalar("Training Loss", epoch_loss / len(dataloader), epoch + 1)


def evaluate(model, dataloader, device, evaluator, epoch, writer):
    model.eval()
    evaluator.clear()
    for images, targets in dataloader:
        images = images.to(device)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        with torch.no_grad():
            outputs = model(images)

        evaluator.update(targets, outputs)

    # Compute evaluation metrics
    metrics = evaluator.coco_eval["bbox"]
    ap = metrics.stats[0]
    f_score = 2 * (metrics.stats[0] * metrics.stats[1]) / (metrics.stats[0] + metrics.stats[1])
    ar = metrics.stats[1]

    # Log metrics to TensorBoard
    writer.add_scalar("mAP", ap, epoch + 1)
    writer.add_scalar("F-score", f_score, epoch + 1)
    writer.add_scalar("mAR", ar, epoch + 1)
def train_faster_rcnn(train_dataset, num_epochs=20, num_classes=2, log_dir="./logs"):
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = torch.nn.Linear(in_features, num_classes)

    return train_model(model, train_dataset, num_epochs, num_classes, log_dir)
