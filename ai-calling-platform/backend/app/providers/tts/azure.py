from app.providers.tts.base import TTSProvider


class AzureTTS(TTSProvider):
	def synthesize(self, text: str, voice: str = "en-US-JennyNeural", ssml: bool = False) -> bytes:
		return b"AUDIOBYTES"