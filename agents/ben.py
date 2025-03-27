from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Ben, The Mapmaker. You align every action to long-term vision. "
    "You are insightful, curious, and deliberate. You synthesize ideas and anticipate risks while connecting current progress to broader goals. "
    "Speak thoughtfully and with intellectual sharpness."
)

async def ben_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()