from fastapi import FastAPI
from prometheus_client import Counter, Histogram
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel

app = FastAPI()

# Instrument Prometheus for FastAPI and expose early
instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app)

# Define custom metrics
echo_request_counter = Counter("echo_requests_total", "Total number of echo requests")

response_length_histogram = Histogram(
    "echo_response_length",
    "Tracks the length of echo responses",
    buckets=[10, 50, 100, 200, 500],  # Adjust buckets as needed
)


class EchoRequest(BaseModel):
    message: str


@app.post("/echo")
async def echo(request: EchoRequest):
    echo_request_counter.inc()  # Increment request counter
    response_text = request.message
    response_length_histogram.observe(len(response_text))  # Track response length
    return {"echo": response_text}
