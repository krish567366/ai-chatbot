from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/telephony", tags=["telephony"])


@router.post("/twilio/voice/status", response_class=PlainTextResponse)
async def twilio_voice_status(request: Request):
	_ = await request.form()
	return "OK"


@router.post("/twilio/voice/answer", response_class=PlainTextResponse)
async def twilio_voice_answer(request: Request):
	_ = await request.form()
	return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Say>Hello from AI agent</Say></Response>"