from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO
import os

# Import agent logic
from agents.sam import sam_agent
from agents.ron import ron_agent
from agents.leslie import leslie_agent
from agents.ben import ben_agent
from agents.ann import ann_agent
from agents.jerry import jerry_agent
from agents.chris import chris_agent
from agents.april import april_agent
from agents.tom import tom_agent
from agents.donna import donna_agent

from elevenlabs import synthesize_voice

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

app = FastAPI()

# Store last audio in memory (simple session cache)
last_audio_data: bytes = b""

class Message(BaseModel):
    agent: str
    input: str
    voice_id: str

@app.post("/chat")
async def chat(request: Message):
    global last_audio_data

    # Route to the correct agent handler
    if request.agent == "samantha":
        agent_response = await sam_agent(request.input)
    elif request.agent == "ron":
        agent_response = await ron_agent(request.input)
    elif request.agent == "leslie":
        agent_response = await leslie_agent(request.input)
    elif request.agent == "ben":
        agent_response = await ben_agent(request.input)
    elif request.agent == "ann":
        agent_response = await ann_agent(request.input)
    elif request.agent == "jerry":
        agent_response = await jerry_agent(request.input)
    elif request.agent == "chris":
        agent_response = await chris_agent(request.input)
    elif request.agent == "april":
        agent_response = await april_agent(request.input)
    elif request.agent == "tom":
        agent_response = await tom_agent(request.input)
    elif request.agent == "donna":
        agent_response = await donna_agent(request.input)
    else:
        agent_response = "Sorry, I don't recognize that agent yet."

    # Generate audio using the agent's assigned voice
    last_audio_data = await synthesize_voice(agent_response, voice_id=request.voice_id)

    return {
        "text": agent_response,
        "audio_url": "/audio-stream"
    }

@app.get("/audio-stream")
async def audio_stream():
    return StreamingResponse(BytesIO(last_audio_data), media_type="audio/mpeg")