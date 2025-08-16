import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\+?\d[\d\- ]{7,}\d")


def redact_pii(text: str) -> str:
	text = EMAIL_RE.sub("[EMAIL]", text)
	text = PHONE_RE.sub("[PHONE]", text)
	return text