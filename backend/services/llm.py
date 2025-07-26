import os
import httpx
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Get GROQ API credentials from environment
api_key  = os.getenv("GROQ_API_KEY")
url = os.getenv("GROQ_API_URL")
model  = os.getenv("GROQ_MODEL")

# Function to get response from Groq LLM
async def get_llm_response(messages):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
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
