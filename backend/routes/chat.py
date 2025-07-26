# backend/routes/chat.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.databases.config import db
from backend.services.llm import get_llm_response
from datetime import datetime
import uuid

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: str = None  # Optional

@router.post("/")
async def chat(req: ChatRequest):
    session_id = req.session_id or str(uuid.uuid4())

    # Create user message dict
    user_message = {
        "role": "user",
        "content": req.message,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Fetch session history for context
    session = db.sessions.find_one({"session_id": session_id})
    history = session["messages"] if session and "messages" in session else []
    
    # Append latest user message to history
    history.append({"role": "user", "content": req.message})

    # Call LLM with full history
    ai_response_text = await get_llm_response(history)

    # Create AI response message
    ai_message = {
        "role": "ai",
        "content": ai_response_text,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Update MongoDB
    db.sessions.update_one(
        {"session_id": session_id},
        {
            "$setOnInsert": {
                "session_id": session_id,
                "user_id": req.user_id,
                "title": req.message[:30]
            },
            "$push": {"messages": {"$each": [user_message, ai_message]}}
        },
        upsert=True
    )

    return {
        "session_id": session_id,
        "user_message": req.message,
        "ai_response": ai_response_text
    }
