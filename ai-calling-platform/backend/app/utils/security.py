from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from app.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
	return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
	return pwd_context.verify(password, password_hash)


def create_jwt(sub: str, tenant_id: int, expires_minutes: int = 60) -> str:
	now = datetime.now(timezone.utc)
	payload = {
		"sub": sub,
		"tid": tenant_id,
		"iat": int(now.timestamp()),
		"exp": int((now + timedelta(minutes=expires_minutes)).timestamp()),
	}
	return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_jwt(token: str) -> Optional[dict]:
	try:
		return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])  # type: ignore
	except Exception:
		return None