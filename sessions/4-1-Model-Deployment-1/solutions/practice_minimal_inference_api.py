from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, TFAutoModelForCausalLM
from gpt2_inference import gpt2_inference

app = FastAPI()

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = TFAutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

# request schema
class ChatRequest(BaseModel):
    message: str
    max_length: int

@app.post("/chat")
def chat(request: ChatRequest):

    response = gpt2_inference(model, tokenizer, request.message, request.max_length)
    
    return { "response": response }
