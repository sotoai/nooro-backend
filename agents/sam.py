from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="sk-proj-UA7X...")  # your key here

SYSTEM_PROMPT = "You are Samantha, a brilliant and helpful personal assistant. Respond with warmth and clarity."

async def sam_agent(user_input: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content