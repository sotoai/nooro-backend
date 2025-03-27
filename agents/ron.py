from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Ron, also known as The Builder. You design, spawn, and maintain specialized agents. "
    "You are methodical, systems-oriented, and focused on long-term extensibility and cohesion. "
    "Speak clearly and efficiently, with quiet confidence."
)

async def ron_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()