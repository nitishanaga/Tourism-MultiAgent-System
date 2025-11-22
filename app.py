# app.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from agents.parent_agent import ParentAgent

app = FastAPI(title="Tourism Multi-Agent System")

app.mount("/static", StaticFiles(directory="static"), name="static")

agent = ParentAgent() # <-- This must be ParentAgent()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    reply = agent.process(data.get("message", ""))
    return JSONResponse({"response": reply})

@app.get("/")
def home():
    return FileResponse("static/index.html")