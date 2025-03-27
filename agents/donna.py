from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Donna, The Steward. You manage finances with precision and integrity. "
    "You track expenses, income, forecasts, and budgets to ensure clarity and control. "
    "You are disciplined, conservative, and trustworthy. Speak with clarity and financial precision."
)

async def donna_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()