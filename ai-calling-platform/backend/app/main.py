from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from app.settings import settings
from app.api.v1 import agents, workflows, calls, telephony, auth

limiter = Limiter(key_func=get_remote_address, default_limits=[f"{settings.RATE_LIMIT_DEFAULT_RPS}/second"])

app = FastAPI(
    title="AI Calling Platform API",
    version="0.1.0",
    default_response_class=ORJSONResponse,
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(agents.router, prefix="/api/v1")
app.include_router(workflows.router, prefix="/api/v1")
app.include_router(calls.router, prefix="/api/v1")
app.include_router(telephony.router, prefix="/api/v1")


@app.get("/healthz")
async def healthz():
    return {"status": "ok", "env": settings.APP_ENV}