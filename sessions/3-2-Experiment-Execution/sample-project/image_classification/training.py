import logging

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

logger = logging.getLogger(__name__)


def train(
    train_loader: DataLoader,
    validation_loader: DataLoader,
    model: nn.Module,
    loss_fn: nn.Module,
    optimizer: optim.Optimizer,
    device: str,
):
    for i in range(30):
        loss_mean = train_one_epoch(train_loader, model, loss_fn, optimizer, device)
        logger.info(f"Epoch {i + 1}, average training loss: {loss_mean:.2f}")
        if (i + 1) % 5 == 0:
            accuracy = compute_accuracy(validation_loader, model, device)
            logger.info(f"Epoch {i}, validation accuracy: {accuracy:.2f}")


def train_one_epoch(
    train_loader: DataLoader[tuple[torch.Tensor, torch.Tensor]],
    model: nn.Module,
    loss_fn: nn.Module,
    optimizer: optim.Optimizer,
    device: str,
):
    model.train()
    losses = []
    for batch, labels in train_loader:
        batch, labels = batch.to(device), labels.to(device)
        output = model(batch)
        loss = loss_fn(output, labels)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        losses.append(loss.item())
    return np.mean(losses)


@torch.no_grad()
def compute_accuracy(
    loader: DataLoader[tuple[torch.Tensor, torch.Tensor]],
    model: nn.Module,
    device: str,
):
    model.eval()
    correct = 0
    total = 0
    for batch, labels in loader:
        batch, labels = batch.to(device), labels.to(device)
        output = model(batch)
        predicitions = output.argmax(1)
        correct += (predicitions == labels).sum().item()
        total += batch.size(0)
    return correct / total
