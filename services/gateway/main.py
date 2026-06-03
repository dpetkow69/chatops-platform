import os, httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from dotenv import load_dotenv

load_dotenv()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")
CHAT_SERVICE_URL = os.getenv("CHAT_SERVICE_URL", "http://chat-service:8002")

app = FastAPI(
    title="ChatOps Gateway",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "gateway"}


@app.post("/auth/register")
async def register(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{AUTH_SERVICE_URL}/register", json=body, timeout=10.0)
    return resp.json()


@app.post("/auth/login")
async def login(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{AUTH_SERVICE_URL}/login", json=body, timeout=10.0)
    return resp.json()


@app.get("/chat/messages")
async def get_messages(request: Request):
    headers = {"Authorization": request.headers.get("Authorization", "")}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CHAT_SERVICE_URL}/messages", headers=headers, timeout=10.0)
    return resp.json()


@app.post("/chat/messages")
async def send_message(request: Request):
    body = await request.json()
    headers = {"Authorization": request.headers.get("Authorization", "")}
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CHAT_SERVICE_URL}/messages", json=body, headers=headers, timeout=10.0)
    return resp.json()
