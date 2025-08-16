from pydantic import BaseModel, Field
from typing import Optional, Literal


class WorkflowOut(BaseModel):
	id: int
	name: str
	state: Literal["draft","published"]
	version_tag: str

	class Config:
		from_attributes = True


class AgentCreate(BaseModel):
	name: str
	locale: str = "en-US"
	voice: str = "en-US-JennyNeural"
	asr_provider: str = "whisper"
	tts_provider: str = "azure"
	llm_provider: str = "openai"
	workflow_id: Optional[int] = None


class AgentOut(BaseModel):
	id: int
	name: str
	locale: str
	voice: str
	asr_provider: str
	tts_provider: str
	llm_provider: str
	workflow: Optional[WorkflowOut]

	class Config:
		from_attributes = True