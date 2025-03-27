import os
import httpx

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"

async def synthesize_voice(text: str, voice_id: str) -> bytes:
    print(f"🔈 [ElevenLabs] Synthesizing voice ID: {voice_id}")
    print(f"📝 [ElevenLabs] Text to synthesize: {text[:100]}...")

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

        print(f"📡 [ElevenLabs] Response status: {response.status_code}")

        if response.status_code != 200:
            print(f"❌ [ElevenLabs] Error response: {response.text}")
            return b""

        return response.content