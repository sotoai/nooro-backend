import httpx
import base64
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# use it in the header
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"

async def synthesize_voice(text: str, voice_id: str) -> str:
    async with httpx.AsyncClient(timeout=30.0) as client:
    response = await client.post(
        f"{BASE_URL}/{voice_id}",
        headers={
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8
            }
        }
    )
        audio_data = response.content
        # Save to file (or stream it later)
        audio_path = f"static/audio_{voice_id}.mp3"
        with open(audio_path, "wb") as f:
            f.write(audio_data)
        return f"/{audio_path}"