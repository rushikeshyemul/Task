# backend/main.py
from fastapi import FastAPI
from backend.routes import chat  
from fastapi import FastAPI
from backend.routes import chat
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import chat
 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev purposes, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat")


@app.get("/")
def root():
    return {"message": "Conversational AI backend running!"}
