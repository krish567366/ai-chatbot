from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import Integer, DateTime, func, Column


class Base(DeclarativeBase):
	pass


class TimestampMixin:
	created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
	updated_at = Column(
		DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
	)


class TenantMixin:
	@declared_attr.directive
	def tenant_id(cls):  # type: ignore
		return Column(Integer, nullable=False, index=True)


class VersionMixin:
	version = Column(Integer, nullable=False, server_default="1")