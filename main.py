from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.sam import sam_agent  # or dynamically route
from elevenlabs import synthesize_voice
from fastapi.staticfiles import StaticFiles
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app = FastAPI()

class Message(BaseModel):
    agent: str
    input: str

@app.post("/chat")
async def chat(request: Message):
    agent_response = await sam_agent(request.input)
    audio_url = await synthesize_voice(agent_response, voice_id="YXpFCvM1S3JbWEJhoskW")  # Samantha
    return {"text": agent_response, "audio_url": audio_url}