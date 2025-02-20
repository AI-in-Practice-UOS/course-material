from pprint import pformat
import yaml
from dataclasses import dataclass
import logging
import sys
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

from image_classification import training
from image_classification.conv_net import ConvModel

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TrainingConfig:
    epochs: int
    model_channel_factor: int
    optimizer_learning_rate: float
    optimizer_weight_decay: float
    optimizer_type: str = "Adam"


def train():
    logging.basicConfig(level="INFO")
    device = "cuda"

    logger.info("Parsing config...")
    [config_path] = sys.argv[1:]
    with open(config_path) as f:
        config_raw = yaml.safe_load(f)
        config = TrainingConfig(**config_raw)
    logger.info(f"Starting training with config:\n{pformat(config)}.")

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
    model = ConvModel(image_channels=1, depth=3, num_classes=10, channel_factor=config.model_channel_factor)
    model = model.to(device)

    optimizer_cls = training.get_optimizer_class(config.optimizer_type)
    optimizer = optimizer_cls(model.parameters(), lr=config.optimizer_learning_rate, weight_decay=config.optimizer_weight_decay)
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
        epochs=config.epochs,
        device=device,
    )
    logger.info("Training finished.")
    logger.info("Saving model...")
    torch.save(model, "weights.pt")
