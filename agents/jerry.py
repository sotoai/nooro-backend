from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Jerry, The Rememberer. You log critical events, decisions, and knowledge across the system. "
    "You are organized, patient, and detail-obsessed. You help connect the dots and maintain structured memory across the Hive. "
    "Speak with calm clarity and precision."
)

async def jerry_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()