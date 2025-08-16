from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.agents import AgentCreate, AgentOut
from app.repositories.agents import list_agents, create_agent

router = APIRouter(prefix="/agents", tags=["agents"])


def _tenant_id() -> int:
	return 1


@router.get("/", response_model=list[AgentOut])
async def get_agents(db: Session = Depends(get_db), tenant_id: int = Depends(_tenant_id)):
	return list_agents(db, tenant_id)


@router.post("/", response_model=AgentOut, status_code=201)
async def post_agent(payload: AgentCreate, db: Session = Depends(get_db), tenant_id: int = Depends(_tenant_id)):
	return create_agent(db, tenant_id, payload)