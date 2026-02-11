from sqlalchemy import Integer, String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin


class Recording(Base, TimestampMixin, TenantMixin):
	__tablename__ = "recordings"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	call_session_id: Mapped[int] = mapped_column(ForeignKey("call_sessions.id"), index=True)
	s3_key: Mapped[str] = mapped_column(String(512))
	duration_seconds: Mapped[int] = mapped_column(Integer, default=0)


class Transcript(Base, TimestampMixin, TenantMixin):
	__tablename__ = "transcripts"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	call_session_id: Mapped[int] = mapped_column(ForeignKey("call_sessions.id"), index=True)
	text: Mapped[str] = mapped_column(String)
	meta: Mapped[dict | None] = mapped_column(JSON)