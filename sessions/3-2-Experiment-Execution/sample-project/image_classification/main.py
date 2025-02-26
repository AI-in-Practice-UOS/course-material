import logging

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

from image_classification import training
from image_classification.conv_net import ConvModel

logger = logging.getLogger(__name__)


def train():
    logging.basicConfig(level="INFO")
    device = "cpu"
    logger.info("Loading Data...")
    train_dataset = datasets.FashionMNIST(
        "data",
        train=True,
        download=True,
        transform=ToTensor(),
    )
    validation_dataset = datasets.FashionMNIST(
        "data",
        train=False,
        download=True,
        transform=ToTensor(),
    )

    logger.info("Initializing model...")
    model = ConvModel(image_channels=1, depth=3, num_classes=10)
    model = model.to(device)

    optimizer = optim.Adam(model.parameters())
    loss_fn = nn.CrossEntropyLoss()
    train_loader = DataLoader(train_dataset, batch_size=128, num_workers=8)
    validation_loader = DataLoader(validation_dataset, batch_size=256, num_workers=8)

    logger.info("Training...")
    training.train(
        train_loader=train_loader,
        validation_loader=validation_loader,
        model=model,
        optimizer=optimizer,
        loss_fn=loss_fn,
        device=device,
    )
    logger.info("Training finished.")
    logger.info("Saving model...")
    torch.save(model, "weights.pt")
