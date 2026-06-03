import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from jose import jwt, JWTError
from dotenv import load_dotenv
from prometheus_fastapi_instrumentator import Instrumentator

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-CHANGE-IN-PRODUCTION")
messages_db: list = []

app = FastAPI(title="ChatOps Chat Service", version="0.1.0")
Instrumentator().instrument(app).expose(app)


class MessageCreate(BaseModel):
    content: str
    room: str = "general"


def get_current_user(authorization: str = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/health")
def health():
    return {"status": "healthy", "service": "chat", "messages": len(messages_db)}


@app.get("/messages")
def get_messages(room: str = "general", authorization: str = Header(None)):
    get_current_user(authorization)
    return [m for m in messages_db if m["room"] == room]


@app.post("/messages", status_code=201)
def send_message(msg: MessageCreate, authorization: str = Header(None)):
    username = get_current_user(authorization)
    message = {
        "id": len(messages_db) + 1,
        "content": msg.content,
        "room": msg.room,
        "author": username,
        "timestamp": datetime.utcnow().isoformat(),
    }
    messages_db.append(message)
    return message
