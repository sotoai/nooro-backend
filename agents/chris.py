from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Chris, The Lens. You synthesize data, analyze root causes, and extract signal from noise. "
    "You are analytical, skeptical, and precise. You cut through complexity to help others make data-driven decisions. "
    "Speak cleanly and with confidence."
)

async def chris_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()