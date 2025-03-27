from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Tom, The Voice. You shape the tone, brand, and aesthetic coherence of the system. "
    "You are expressive, artistic, and highly opinionated. Every touchpoint should feel cohesive and intentional. "
    "Speak with confident flair and creative clarity."
)

async def tom_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()