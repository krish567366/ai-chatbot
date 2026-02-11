from typing import Dict, Any


class WorkflowEngine:
	def __init__(self, dsl: Dict[str, Any]):
		self.dsl = dsl
		self.node_index = {n["id"]: n for n in dsl.get("nodes", [])}
		self.edges = dsl.get("edges", [])

	def next_nodes(self, current_id: str) -> list[str]:
		return [e["target"] for e in self.edges if e["source"] == current_id]