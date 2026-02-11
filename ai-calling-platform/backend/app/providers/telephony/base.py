from typing import Protocol, Any, Dict


class TelephonyProvider(Protocol):
	def place_call(self, to_number: str, from_number: str, webhook_base: str, metadata: Dict[str, Any] | None = None) -> str:
		...

	def provision_number(self, area_code: str | None = None) -> str:
		...

	def release_number(self, phone_number: str) -> None:
		...