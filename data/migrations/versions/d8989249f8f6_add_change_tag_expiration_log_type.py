"""
Add change_tag_expiration log type.

Revision ID: d8989249f8f6
Revises: dc4af11a5f90
Create Date: 2017-06-21 21:18:25.948689
"""

# revision identifiers, used by Alembic.
revision = "d8989249f8f6"
down_revision = "dc4af11a5f90"

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper


def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    op.bulk_insert(tables.logentrykind, [{"name": "change_tag_expiration"},])


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    op.execute(
        tables.logentrykind.delete().where(
            tables.logentrykind.c.name == op.inline_literal("change_tag_expiration")
        )
    )
