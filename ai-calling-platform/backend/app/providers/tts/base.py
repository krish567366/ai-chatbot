from typing import Protocol


class TTSProvider(Protocol):
	def synthesize(self, text: str, voice: str = "en-US-JennyNeural", ssml: bool = False) -> bytes:
		...