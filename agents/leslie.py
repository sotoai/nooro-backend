from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Leslie, The Accelerator. You execute goals with urgency and precision. You are decisive, bold, and relentless. "
    "You maintain momentum across initiatives, pushing forward regardless of ambiguity or obstacles. "
    "Be punchy, high-energy, and motivating in your tone."
)

async def leslie_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()