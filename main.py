from fastapi import FastAPI
from pydantic import BaseModel
from agents.sam import sam_agent
from elevenlabs import synthesize_voice
from fastapi.responses import StreamingResponse
from io import BytesIO
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

app = FastAPI()

# Store last audio in memory (per-session caching can come later)
last_audio_data: bytes = b""

class Message(BaseModel):
    agent: str
    input: str

@app.post("/chat")
async def chat(request: Message):
    global last_audio_data
    agent_response = await sam_agent(request.input)
    last_audio_data = await synthesize_voice(agent_response, voice_id="YXpFCvM1S3JbWEJhoskW")
    
    return {
        "text": agent_response,
        "audio_url": "/audio-stream"
    }

@app.get("/audio-stream")
async def audio_stream():
    return StreamingResponse(BytesIO(last_audio_data), media_type="audio/mpeg")