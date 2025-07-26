# backend/routes/chat.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.databases.config import db
from backend.databases.schema import Message
from datetime import datetime
from bson import ObjectId
import uuid
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import chat

router = APIRouter()
users_collection = db["users"]



@router.get("/")
def check_status():
    return {"msg": "Chat API working!"}

class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: str = None

@router.post("/api/chat")
def chat(request: ChatRequest):
    # Step 1: Validate user
    user = users_collection.find_one({"user_id": request.user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    # Step 2: Create new session if session_id not given
    session_id = request.session_id
    if not session_id:
        session_id = str(uuid.uuid4())
        session = {
            "session_id": session_id,
            "title": f"Chat on {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}",
            "messages": []
        }
        users_collection.update_one(
            {"user_id": request.user_id},
            {"$push": {"sessions": session}}
        )

    # Step 3: Save user message
    user_msg = Message(role="user", content=request.message)
    users_collection.update_one(
        {"user_id": request.user_id, "sessions.session_id": session_id},
        {"$push": {"sessions.$.messages": user_msg.dict()}}
    )

    # Step 4: Generate fake AI response (replace with real model later)
    ai_response_content = f"You said: {request.message}"
    ai_msg = Message(role="ai", content=ai_response_content)
    users_collection.update_one(
        {"user_id": request.user_id, "sessions.session_id": session_id},
        {"$push": {"sessions.$.messages": ai_msg.dict()}}
    )

    # Step 5: Return AI response
    return {
        "session_id": session_id,
        "user_message": user_msg,
        "ai_response": ai_msg
    }
