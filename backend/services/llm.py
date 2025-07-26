import os
import httpx
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Get GROQ API credentials from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-70b-8192"

# Function to get response from Groq LLM
async def get_llm_response(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=payload)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        response.raise_for_status()  # Will raise error for non-2xx codes

        data = response.json()
        return data["choices"][0]["message"]["content"]

# Testing block (runs when file is executed directly)
if __name__ == "__main__":
    test_messages = [
        {"role": "user", "content": "Hello! What is the capital of India?"}
    ]

    async def test():
        result = await get_llm_response(test_messages)
        print("LLM Output:", result)

    asyncio.run(test())
