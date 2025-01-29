from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoRequest(BaseModel):
    message: str

@app.post("/echo")
async def echo(request: EchoRequest):
    return {"echo": request.message}

