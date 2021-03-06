"""
Change LogEntry to use a BigInteger as its primary key.

Revision ID: 6c21e2cfb8b6
Revises: d17c695859ea
Create Date: 2018-07-27 16:30:02.877346
"""

# revision identifiers, used by Alembic.
revision = "6c21e2cfb8b6"
down_revision = "d17c695859ea"

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa


def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    op.alter_column(
        table_name="logentry",
        column_name="id",
        nullable=False,
        autoincrement=True,
        type_=sa.BigInteger(),
    )


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    op.alter_column(
        table_name="logentry",
        column_name="id",
        nullable=False,
        autoincrement=True,
        type_=sa.Integer(),
    )
