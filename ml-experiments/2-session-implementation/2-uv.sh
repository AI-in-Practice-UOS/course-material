## Create a new package
# https://docs.astral.sh/uv/concepts/projects/init/#packaged-applications
uv init DIR --package --name NAME
cd DIR

## Explain structure

## Install Python interpreter from .python-version
uv python install

## Add a dependency (numpy has no dependencies itself)
# Also initializes the virtual env in .venv
uv add numpy

## Show lockfile

## Add another (requests has dependencies itself)
uv add requests

## Show dependency tree
uv tree

## Show that lockfile also contains implicit dependencies

## Show commands defined in pyproject.toml
# Run src/NAME/main.py
uv run NAME

## Explain that `python` only works if the .venv is activated
# Usually only `uv` is needed

## Remove a package
uv remove requests

## Upgrade package
uv lock --upgrade-package numpy

## Installing packages for an existing project
uv sync
