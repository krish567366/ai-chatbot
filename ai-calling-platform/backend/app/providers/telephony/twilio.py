import httpx
from typing import Any, Dict
from app.settings import settings


class TwilioProvider:
	def __init__(self, account_sid: str | None = None, auth_token: str | None = None):
		self.account_sid = account_sid or settings.TWILIO_ACCOUNT_SID or ""
		self.auth_token = auth_token or settings.TWILIO_AUTH_TOKEN or ""
		self.base = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}"

	def place_call(self, to_number: str, from_number: str, webhook_base: str, metadata: Dict[str, Any] | None = None) -> str:
		url = f"{self.base}/Calls.json"
		data = {
			"To": to_number,
			"From": from_number,
			"Url": f"{webhook_base}/api/v1/telephony/twilio/voice/answer",
			"StatusCallback": f"{webhook_base}/api/v1/telephony/twilio/voice/status",
			"StatusCallbackEvent": ["initiated","ringing","answered","completed"],
		}
		with httpx.Client(auth=(self.account_sid, self.auth_token), timeout=10.0) as client:
			resp = client.post(url, data=data)
			resp.raise_for_status()
			return resp.json().get("sid", "")

	def provision_number(self, area_code: str | None = None) -> str:
		return "+12025550123"

	def release_number(self, phone_number: str) -> None:
		return None