from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.agents import Agent
from app.schemas.agents import AgentCreate


def create_agent(db: Session, tenant_id: int, data: AgentCreate) -> Agent:
	agent = Agent(
		tenant_id=tenant_id,
		name=data.name,
		locale=data.locale,
		voice=data.voice,
		asr_provider=data.asr_provider,
		tts_provider=data.tts_provider,
		llm_provider=data.llm_provider,
		workflow_id=data.workflow_id,
	)
	db.add(agent)
	db.commit()
	db.refresh(agent)
	return agent


def list_agents(db: Session, tenant_id: int) -> list[Agent]:
	stmt = select(Agent).where(Agent.tenant_id == tenant_id)
	return list(db.execute(stmt).scalars().all())