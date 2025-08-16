from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from app.settings import settings
from app.api.v1 import agents, workflows, calls, telephony

app = FastAPI(
    title="AI Calling Platform API",
    version="0.1.0",
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents.router, prefix="/api/v1")
app.include_router(workflows.router, prefix="/api/v1")
app.include_router(calls.router, prefix="/api/v1")
app.include_router(telephony.router, prefix="/api/v1")


@app.get("/healthz")
async def healthz():
    return {"status": "ok", "env": settings.APP_ENV}