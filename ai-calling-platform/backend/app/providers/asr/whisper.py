from app.providers.asr.base import ASRProvider


class WhisperASR(ASRProvider):
	def transcribe(self, audio_bytes: bytes, language: str = "en-US") -> str:
		return "transcribed text"