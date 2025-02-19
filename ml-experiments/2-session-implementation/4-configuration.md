# Configuration

## Python's `dataclasses`

Basic usage:
```python
from dataclasses import dataclass

@dataclass
class ExperimentConfig:
    learning_rate: float
    weight_decay: float = 0.0001
    optimizer: str = "Adam"

config = ExperimentConfig(learning_rate=0.01)

print(config.optimizer)
```

## Features
* Automatic generation of various dunder methods.
* 
