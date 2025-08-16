from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20240816_0002'
down_revision = '20240816_0001'
branch_labels = None
depends_on = None

def upgrade() -> None:
	op.create_table(
		"recordings",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("call_session_id", sa.Integer(), sa.ForeignKey("call_sessions.id"), index=True),
		sa.Column("s3_key", sa.String(length=512), nullable=False),
		sa.Column("duration_seconds", sa.Integer(), server_default="0"),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)

	op.create_table(
		"transcripts",
		sa.Column("id", sa.Integer(), primary_key=True),
		sa.Column("tenant_id", sa.Integer(), nullable=False, index=True),
		sa.Column("call_session_id", sa.Integer(), sa.ForeignKey("call_sessions.id"), index=True),
		sa.Column("text", sa.Text(), nullable=False),
		sa.Column("meta", sa.JSON()),
		sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
		sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
	)


def downgrade() -> None:
	op.drop_table("transcripts")
	op.drop_table("recordings")