"""Create tasks table

Revision ID: 0490cc4870b6
Revises: 80a8cbfc3107
Create Date: 2024-10-21 01:20:05.277660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0490cc4870b6'
down_revision: Union[str, None] = '80a8cbfc3107'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'description',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               nullable=False)
    op.alter_column('tasks', 'due_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_index('ix_tasks_description', table_name='tasks')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tasks_description', 'tasks', ['description'], unique=False)
    op.alter_column('tasks', 'due_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('tasks', 'description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               nullable=True)
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('tasks', 'created_at')
    # ### end Alembic commands ###
