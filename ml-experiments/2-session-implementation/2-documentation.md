# 1 - Documentation

Proper documentation of experiments, datasets and code is critical for transparent and reproducible experiments.

## High-level Experiment Information
 
Serves as first entrypoint to an experiment, containing:

- Metadata: description, hypothesis etc.
- References to data, configuration, state of experiment code and tracked results.
- Analysis and discussion of results.

Where each experiment is documented separately.

## Data

We don't cover tools for storage of concrete data because this topic highly depends on the problem domain (vision, language etc.) and the tools to choose from are endless.

Conversly, metadata is largely independent of the data type, information such as:
- Owner
- Description
- Version
- Creation Date
- ...

should be documented and can thus be stored in a unified way.

## Code

Code can be documented on different levels, a simple differentation is:

- API / Low-level: Use, inputs and outputs of every function and class.
- High-level: Main entrypoints. How different parts of the code work together.

For ML experiments, you should document high-level functions such as training and data pipelines first.

## Notion

- Notion is a highly versatile and easy-to-use tool.
- Its database functionality provides excellent capabilities to track information about data and experiments.
- Futhermore, its primary use case is building knowlege bases, making it a good choice for documenting code as well.

> *Hands-on showcase*

<!---
Final state: https://www.notion.so/ML-Experiments-19f00b4f2fbf80ffae62c7eccd3f6e79
-->