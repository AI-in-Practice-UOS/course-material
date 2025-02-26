# Sample Project

## Setup

Install [`uv`](https://docs.astral.sh/uv/).
```bash
# Linux / Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Execute the following instructions inside the project directory.

(Optional) Install the python interpreter specified in `.python-version`.
```bash
uv python install
```

Setup the Python virtual environment and install the dependencies.
```bash
uv sync
```

## Usage

[Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) (Python packages).

Run training.
```bash
uv run train
```
