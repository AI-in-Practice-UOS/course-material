import logging
from fastapi import FastAPI, HTTPException
from gpt2_inference import gpt2_inference
from pydantic import BaseModel, Field, model_validator
from transformers import AutoTokenizer, TFAutoModelForCausalLM
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram


app = FastAPI(
    title="Inference API",
    description="API for inference with distilled GPT2 model",
    version="1.0"
)
Instrumentator().instrument(app).expose(app)

llm_request_counter = Counter(
    "llm_requests_total", "Total number of chat requests"
)

llm_response_length_histogram = Histogram(
    "llm_response_length", "Tracks the length of model-generated responses",
    buckets=[10, 50, 100, 200, 500, 1000, 2000]
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting to load tokenizer and model")

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = TFAutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

logger.info("Finished loading tokenizer and model")

# request schema
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=100, example="The meaning of life is", description="Message to complete using the language model")
    max_length: int = Field(..., gt=1, le=200, example=50, description="Number of output tokens, including the input message")

    @model_validator(mode="after")
    def validate_max_tokens(self):
        """Ensure that the output max length is greater than the input tokens."""
        message_token_num = len(tokenizer(self.message)["input_ids"])
        if self.max_length <= message_token_num:
            raise ValueError(f"Maximum length must be greater then the number of message tokens ({message_token_num})")
        return self
    
# response schema
class ChatResponse(BaseModel):
    response: str = Field(..., description="Response from the language model")

# error response
class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error details")
    
@app.post(
    "/chat",
    response_model=ChatResponse,
    summary="Generate a message",
    responses={
        200: {"description": "Response generated"},
        500: {"description": "Language model error", "model": ErrorResponse},
    },
)
def chat(request: ChatRequest):
    """Generate response using a language model"""

    llm_request_counter.inc()
    logger.info("Request with max length %d for message: '%s'", request.max_length, request.message)

    try:
        response = gpt2_inference(model, tokenizer, request.message, request.max_length)
    except Exception as e:
        logger.error("Error while calling the language model: %s", e)

        raise HTTPException(
            status_code=500,
            detail="An error occurred while calling the language model"
        )
    
    llm_response_length_histogram.observe(len(response))
    logger.info("Generated message: '%s'", response)
    
    return { "response": response }
