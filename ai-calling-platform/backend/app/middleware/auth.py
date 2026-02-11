from fastapi import Depends, HTTPException, Header
from app.utils.security import decode_jwt


def current_tenant_id(authorization: str | None = Header(default=None)) -> int:
	if not authorization or not authorization.startswith("Bearer "):
		raise HTTPException(status_code=401, detail="Missing token")
	token = authorization.split(" ", 1)[1]
	payload = decode_jwt(token)
	if not payload:
		raise HTTPException(status_code=401, detail="Invalid token")
	return int(payload.get("tid", 0))