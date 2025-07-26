# backend/database/schema.py

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from typing import Optional

class ChatMessage(BaseModel):
    user_id: str
    message: str
    conversation_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Message(BaseModel):
    role: str  # 'user' or 'ai'
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Session(BaseModel):
    session_id: str
    title: str
    messages: List[Message] = []

class User(BaseModel):
    user_id: str
    username: str
    email: str
    sessions: List[Session] = []
