# Configuration

Definition: Configuration compasses the parameters that impact the outcome of an experiment.

Common problematic practices:
- Hard coding configuration anywhere in the code base.
- Using Python dictionaries to define configuration.

We will be using dataclasses as a simple but effective solution to implement configuration tracking.

## Python's `dataclasses`
Idea: Add all configuration parameters as attributes to a Python class.

Can be accomplished with regular Python classes, but `dataclasses` eases the implementation and provides additional features. In particular, the `dataclass` decorator generates various dunder methods, for example `__init__` or `__eq__`.

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

## Advantages 
* Clear, typed definition of parameters.
* Validation of field names.
* Single source of truth.
* Type checker can provide intellisense and detect bugs.
* Easly initialized from configurations stored in YAML or JSON.
* Contained in standard library.

---
> *Hands-on showcase in sample project*