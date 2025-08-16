from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.base import Base, TimestampMixin


class Tenant(Base, TimestampMixin):
	__tablename__ = "tenants"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
	domain: Mapped[str | None] = mapped_column(String(255), unique=True)

	users = relationship("User", back_populates="tenant")


class Role(Base):
	__tablename__ = "roles"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)


class User(Base, TimestampMixin):
	__tablename__ = "users"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), nullable=False, index=True)
	email: Mapped[str] = mapped_column(String(255), nullable=False)
	password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True)

	tenant = relationship("Tenant", back_populates="users")

	__table_args__ = (
		UniqueConstraint("tenant_id", "email", name="uq_users_tenant_email"),
	)


class APIKey(Base, TimestampMixin):
	__tablename__ = "api_keys"
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), index=True)
	key_hash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
	label: Mapped[str] = mapped_column(String(128), nullable=False)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True)