"""empty message

Revision ID: 532495655068
Revises: 
Create Date: 2018-10-25 13:19:29.027259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "532495655068"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("hash", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("hash"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("table")
    # ### end Alembic commands ###
