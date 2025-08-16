from typing import Protocol


class ASRProvider(Protocol):
	def transcribe(self, audio_bytes: bytes, language: str = "en-US") -> str:
		...