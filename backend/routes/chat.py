# backend/routes/chat.py
# backend/routes/chat.py
from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, HTTPException
from backend.routes import chat
from backend.databases.config import db
from backend.databases.schema import Message


from bson import ObjectId
from datetime import datetime

router = APIRouter()

users_collection = db["users"]

@router.get("/")
async def hello():
    return {"msg": "Chat API working!"}

@router.post("/add_message")
def add_message(user_id: str, session_id: str, role: str, content: str):
    message = Message(role=role, content=content)
    result = users_collection.update_one(
        {"user_id": user_id, "sessions.session_id": session_id},
        {"$push": {"sessions.$.messages": message.dict()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User or session not found.")
    return {"status": "Message added", "message": message}

@router.post("/start_session")
def start_session(user_id: str, session_id: str, title: str):
    session = {
        "session_id": session_id,
        "title": title,
        "messages": []
    }
    result = users_collection.update_one(
        {"user_id": user_id},
        {"$push": {"sessions": session}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"status": "Session started", "session": session}

@router.post("/create_user")
def create_user(user_id: str, username: str, email: str):
    if users_collection.find_one({"user_id": user_id}):
        return {"status": "User already exists"}
    user = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "sessions": []
    }
    users_collection.insert_one(user)
    return {"status": "User created", "user": user}
