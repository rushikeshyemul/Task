# backend/main.py
from fastapi import FastAPI
from backend.routes import chat  
from fastapi import FastAPI
from backend.routes import chat

 

app = FastAPI()
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "Conversational AI backend running!"}
