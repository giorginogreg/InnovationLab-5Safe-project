import torch
from torch.utils.data import DataLoader
from torchvision import models
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from torch.utils.tensorboard import SummaryWriter
from logs_utils.logger import logger

def collate_fn(batch):
    return tuple(zip(*batch))
def train_model(
    model, train_dataset, num_epochs=20, num_classes=2, log_dir="./logs"
):
    """
    Train the model on the specified dataset.

    Args:
        model (torch.nn.Module): The model to train.
        train_dataset (torch.utils.data.Dataset): The training dataset.
        num_epochs (int): Number of epochs to train for.
        num_classes (int): Number of classes in the dataset.
        log_dir (str): Directory to save the logs.

    Returns:
        torch.nn.Module: The trained model.
    """
    train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True, collate_fn=collate_fn)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    # Learning rate scheduler
    lr_scheduler = torch.optim.lr_scheduler.StepLR(
        optimizer, step_size=3, gamma=0.1
    )

    # TensorBoard writer
    writer = SummaryWriter(log_dir=log_dir)

    # Initialize COCO evaluator
    coco_gt = COCO(annotation_file="./resources/annotations/training.json")
    evaluator = COCOeval(coco_gt)

    best_epoch = -1
    best_map = -1

    for epoch in range(num_epochs):
        train_one_epoch(
            model,
            train_dataloader,
            optimizer,
            device,
            epoch,
            writer,
            num_epochs,
        )
        evaluate(model, train_dataloader, device, evaluator, epoch, writer)
        lr_scheduler.step()

        # Save checkpoint
        if (epoch + 1) % 5 == 0:
            checkpoint_path = f"checkpoint_epoch_{epoch+1}.pth"
            torch.save(model.state_dict(), checkpoint_path)
            print(f"Saved checkpoint: {checkpoint_path}")

        # Check if current epoch has the best mAP
        if evaluator.stats[0] > best_map:
            best_epoch = epoch + 1
            best_map = evaluator.stats[0]

    print(f"Best epoch: {best_epoch}, Best mAP: {best_map}")

    writer.close()

    return model


def train_one_epoch(
    model, dataloader, optimizer, device, epoch, writer, num_epochs
):
    """
    Train the model for one epoch.

    Args:
        model (torch.nn.Module): The model to train.
        dataloader (torch.utils.data.DataLoader): DataLoader for the training dataset.
        optimizer (torch.optim.Optimizer): Optimizer for training.
        device (torch.device): Device (CPU or GPU) to perform training on.
        epoch (int): Current epoch number.
        writer (torch.utils.tensorboard.SummaryWriter): TensorBoard writer for logging.
        num_epochs (int): Total number of epochs.

    Returns:
        None
    """
    model.train()
    epoch_loss = 0.0
    logger.info(list(dataloader))
    exit()
    for images, targets in dataloader:
        logger.info(images)
        images = images.to(device)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        optimizer.zero_grad()
        outputs = model(images, targets)
        loss = sum(loss for loss in outputs.values())
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(
        f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss/len(dataloader):.4f}"
    )

    # Log training loss to TensorBoard
    writer.add_scalar("Training Loss", epoch_loss / len(dataloader), epoch + 1)


def evaluate(model, dataloader, device, evaluator, epoch, writer):
    """
    Evaluate the model on the validation dataset and log evaluation metrics.

    Args:
        model (torch.nn.Module): The trained model to evaluate.
        dataloader (torch.utils.data.DataLoader): DataLoader for the validation dataset.
        device (torch.device): Device (CPU or GPU) to perform the evaluation on.
        evaluator (pycocotools.cocoeval.COCOeval): COCO evaluator object.
        epoch (int): Current epoch number.
        writer (torch.utils.tensorboard.SummaryWriter): TensorBoard writer for logging.

    Returns:
        None
    """
    model.eval()
    evaluator.cocoDt = []  # Reset cocoDt list
    for images, targets in dataloader:
        images = images.to(device)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        with torch.no_grad():
            outputs = model(images)

        # Convert model outputs to COCO format
        converted_outputs = []
        for i in range(len(outputs)):
            # Convert output i to COCO format
            boxes = outputs[i]["boxes"].cpu().numpy()
            scores = outputs[i]["scores"].cpu().numpy()
            labels = outputs[i]["labels"].cpu().numpy()

            converted_output = {
                "image_id": targets[i]["image_id"].item(),
                "category_id": labels,
                "bbox": boxes.tolist(),
                "score": scores.tolist(),
            }

            converted_outputs.append(converted_output)

        # Append converted outputs to cocoDt list
        evaluator.cocoDt.extend(converted_outputs)

    # Run COCO evaluation
    evaluator.evaluate()
    evaluator.accumulate()
    evaluator.summarize()

    # Retrieve evaluation metrics
    ap = evaluator.stats[0]
    f_score = (
        2
        * (evaluator.stats[0] * evaluator.stats[1])
        / (evaluator.stats[0] + evaluator.stats[1])
    )
    ar = evaluator.stats[1]

    # Log metrics to TensorBoard
    writer.add_scalar("mAP", ap, epoch + 1)
    writer.add_scalar("F-score", f_score, epoch + 1)
    writer.add_scalar("mAR", ar, epoch + 1)


def train_faster_rcnn(
    train_dataset, num_epochs=20, num_classes=2, log_dir="./logs"
):
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = torch.nn.Linear(in_features, num_classes)

    return train_model(model, train_dataset, num_epochs, num_classes, log_dir)
