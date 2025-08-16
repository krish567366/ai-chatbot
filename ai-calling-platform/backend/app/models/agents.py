from sqlalchemy import Integer, String, Boolean, ForeignKey, JSON, Enum, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin, TenantMixin, VersionMixin
import enum


class WorkflowState(str, enum.Enum):
	draft = "draft"
	published = "published"


class Agent(Base, TimestampMixin, TenantMixin, VersionMixin):
	__tablename__ = "agents"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name: Mapped[str] = mapped_column(String(255), nullable=False)
	locale: Mapped[str] = mapped_column(String(16), default="en-US")
	voice: Mapped[str] = mapped_column(String(64), default="en-US-JennyNeural")
	asr_provider: Mapped[str] = mapped_column(String(64), default="whisper")
	tts_provider: Mapped[str] = mapped_column(String(64), default="azure")
	llm_provider: Mapped[str] = mapped_column(String(64), default="openai")
	workflow_id: Mapped[int | None] = mapped_column(ForeignKey("workflows.id"))

	workflow = relationship("Workflow", back_populates="agents")


class Workflow(Base, TimestampMixin, TenantMixin, VersionMixin):
	__tablename__ = "workflows"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name: Mapped[str] = mapped_column(String(255), nullable=False)
	state: Mapped[WorkflowState] = mapped_column(Enum(WorkflowState), default=WorkflowState.draft)
	version_tag: Mapped[str] = mapped_column(String(64), default="v1")

	agents = relationship("Agent", back_populates="workflow")
	nodes = relationship("Node", back_populates="workflow", cascade="all, delete-orphan")
	edges = relationship("Edge", back_populates="workflow", cascade="all, delete-orphan")

	__table_args__ = (
		Index("ix_workflows_tenant_state", "tenant_id", "state"),
	)


class Node(Base, TimestampMixin, TenantMixin):
	__tablename__ = "nodes"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	workflow_id: Mapped[int] = mapped_column(ForeignKey("workflows.id"), index=True)
	type: Mapped[str] = mapped_column(String(64), nullable=False)
	config: Mapped[dict] = mapped_column(JSON, default=dict)

	workflow = relationship("Workflow", back_populates="nodes")


class Edge(Base, TimestampMixin, TenantMixin):
	__tablename__ = "edges"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	workflow_id: Mapped[int] = mapped_column(ForeignKey("workflows.id"), index=True)
	source_node_id: Mapped[int] = mapped_column(ForeignKey("nodes.id"))
	target_node_id: Mapped[int] = mapped_column(ForeignKey("nodes.id"))
	condition: Mapped[dict | None] = mapped_column(JSON)

	workflow = relationship("Workflow", back_populates="edges")


class CallSession(Base, TimestampMixin, TenantMixin):
	__tablename__ = "call_sessions"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), index=True)
	status: Mapped[str] = mapped_column(String(32), default="created")
	metadata: Mapped[dict | None] = mapped_column(JSON)