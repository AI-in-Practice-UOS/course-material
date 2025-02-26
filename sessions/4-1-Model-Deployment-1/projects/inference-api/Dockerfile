# adapted from https://docs.astral.sh/uv/guides/integration/fastapi

# Define base image.
FROM python:3.11-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working dir.
WORKDIR /app

# Copy uv dependencies.
COPY pyproject.toml uv.lock ./

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY . .

# Indicate the port for correct usage.
EXPOSE 80

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]

