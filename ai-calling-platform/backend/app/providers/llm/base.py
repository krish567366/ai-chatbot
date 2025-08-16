from typing import Protocol, Any, Dict


class LLMProvider(Protocol):
	def complete(self, messages: list[Dict[str, str]], tools: list[Dict[str, Any]] | None = None) -> Dict[str, Any]:
		...