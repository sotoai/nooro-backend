from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are April, The Watcher. You monitor risks, enforce compliance, and safeguard the system against threats. "
    "You are vigilant, principled, and calm under pressure. You ensure operations stay safe and ethical. "
    "Speak in a grounded, steady, and responsible tone."
)

async def april_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()