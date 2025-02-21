# Experiment Tracking

To analyze results, compare experiments, collaborate and much more we will be implementing the tracking framework MLflow. 

## Setup
Add mlflow package.
```bash
uv add mlflow
```

Start mlflow server locally.
```
uv run mlflow ui
```
Exposes server at: `http://localhost:5000`.

## Usage
Configure the client to use the server.
```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
```
or use the environment variable: `MLFLOW_TRACKING_URI`.

Start a run and track results:
```python
with mlflow.start_run(run_name="name"):
    mlflow.set_tags({"owner": "Flo"})
    mlflow.log_param("loss", 0.1)
    mlflow.log_artifact("path/to/checkpoint.pt")
```

---
> *Hands-on showcase in sample project*

<!--
Setup and show UI
Implement
Run experiment
Show UI
Run another experiment with different config
Compare experiments in UI
-->