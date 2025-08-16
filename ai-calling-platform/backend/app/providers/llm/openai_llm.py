from typing import Any, Dict
from app.providers.llm.base import LLMProvider


class OpenAILLM(LLMProvider):
	def complete(self, messages: list[Dict[str, str]], tools: list[Dict[str, Any]] | None = None) -> Dict[str, Any]:
		return {"content": "Hello, how can I help you?", "tool_calls": []}