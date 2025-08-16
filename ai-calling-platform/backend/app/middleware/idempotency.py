from fastapi import Header, HTTPException
import hashlib
import redis
from app.settings import settings

_r = redis.Redis.from_url(settings.REDIS_URL)


def enforce_idempotency(idempotency_key: str | None = Header(default=None)) -> None:
	if not idempotency_key:
		return
	digest = hashlib.sha256(idempotency_key.encode()).hexdigest()
	# set-if-not-exists with expiry (5 minutes)
	ok = _r.set(name=f"idem:{digest}", value="1", nx=True, ex=300)
	if not ok:
		raise HTTPException(status_code=409, detail="Idempotency key already used")