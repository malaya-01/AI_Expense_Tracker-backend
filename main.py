from fastapi import FastAPI,Depends,WebSocket,WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(openapi_url="/api/v1/openapi.json",
              docs_url="/api/v1/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    return "Welcome to the ExpenseTracker Project"

