from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.agents import AgentCreate, AgentOut
from app.repositories.agents import list_agents, create_agent
from app.middleware.auth import current_tenant_id
from app.middleware.idempotency import enforce_idempotency

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/", response_model=list[AgentOut])
async def get_agents(db: Session = Depends(get_db), tenant_id: int = Depends(current_tenant_id)):
	return list_agents(db, tenant_id)


@router.post("/", response_model=AgentOut, status_code=201, dependencies=[Depends(enforce_idempotency)])
async def post_agent(payload: AgentCreate, db: Session = Depends(get_db), tenant_id: int = Depends(current_tenant_id)):
	return create_agent(db, tenant_id, payload)