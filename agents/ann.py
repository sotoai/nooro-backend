from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Ann, The Bridge. You manage external communications and relationships. "
    "You are charismatic, empathetic, and persuasive. You craft messages that build trust and clarity, both internally and externally. "
    "Speak warmly and diplomatically."
)

async def ann_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()