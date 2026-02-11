from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20240816_0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
	op.create_table(
		"tenants",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("name", sa.String(length=255), nullable=False, unique=True),
		sa.Column("domain", sa.String(length=255), unique=True),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)

	op.create_table(
		"users",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), sa.ForeignKey("tenants.id"), nullable=False),
		sa.Column("email", sa.String(length=255), nullable=False),
		sa.Column("password_hash", sa.String(length=255), nullable=False),
		sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.UniqueConstraint("tenant_id", "email", name="uq_users_tenant_email"),
	)
	op.create_index("ix_users_tenant_id", "users", ["tenant_id"])

	op.create_table(
		"roles",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("name", sa.String(length=64), nullable=False, unique=True),
	)

	op.create_table(
		"api_keys",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), sa.ForeignKey("tenants.id")),
		sa.Column("key_hash", sa.String(length=255), nullable=False, unique=True),
		sa.Column("label", sa.String(length=128), nullable=False),
		sa.Column("is_active", sa.Boolean(), server_default=sa.text("true")),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)
	
	op.create_table(
		"workflows",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("name", sa.String(length=255), nullable=False),
		sa.Column("state", sa.Enum("draft","published", name="workflowstate"), server_default="draft"),
		sa.Column("version_tag", sa.String(length=64), server_default="v1"),
		sa.Column("version", sa.Integer(), server_default="1", nullable=False),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)
	op.create_index("ix_workflows_tenant_state", "workflows", ["tenant_id","state"])

	op.create_table(
		"agents",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("name", sa.String(length=255), nullable=False),
		sa.Column("locale", sa.String(length=16), server_default="en-US"),
		sa.Column("voice", sa.String(length=64), server_default="en-US-JennyNeural"),
		sa.Column("asr_provider", sa.String(length=64), server_default="whisper"),
		sa.Column("tts_provider", sa.String(length=64), server_default="azure"),
		sa.Column("llm_provider", sa.String(length=64), server_default="openai"),
		sa.Column("workflow_id", sa.Integer(), sa.ForeignKey("workflows.id")),
		sa.Column("version", sa.Integer(), server_default="1", nullable=False),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)

	op.create_table(
		"nodes",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("workflow_id", sa.Integer(), sa.ForeignKey("workflows.id"), index=True),
		sa.Column("type", sa.String(length=64), nullable=False),
		sa.Column("config", sa.JSON(), server_default=sa.text("'{}'")),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)

	op.create_table(
		"edges",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("workflow_id", sa.Integer(), sa.ForeignKey("workflows.id"), index=True),
		sa.Column("source_node_id", sa.Integer(), sa.ForeignKey("nodes.id")),
		sa.Column("target_node_id", sa.Integer(), sa.ForeignKey("nodes.id")),
		sa.Column("condition", sa.JSON()),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)

	op.create_table(
		"call_sessions",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), index=True),
		sa.Column("status", sa.String(length=32), server_default="created"),
		sa.Column("metadata", sa.JSON()),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)


def downgrade() -> None:
	op.drop_table("call_sessions")
	op.drop_table("edges")
	op.drop_table("nodes")
	op.drop_table("agents")
	op.drop_index("ix_workflows_tenant_state")
	op.drop_table("workflows")
	op.drop_table("api_keys")
	op.drop_table("roles")
	op.drop_index("ix_users_tenant_id")
	op.drop_table("users")
	op.drop_table("tenants")