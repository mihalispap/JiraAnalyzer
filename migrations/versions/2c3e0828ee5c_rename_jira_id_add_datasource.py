"""rename jira_id // add datasource

Revision ID: 2c3e0828ee5c
Revises: d796e5f60e30
Create Date: 2024-01-27 15:39:35.886813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c3e0828ee5c'
down_revision: Union[str, None] = 'd796e5f60e30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('external_id', sa.String(length=256), nullable=False))
    op.add_column('project', sa.Column('datasource', sa.String(length=256), nullable=False))
    op.drop_column('project', 'jira_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('jira_id', sa.VARCHAR(length=256), nullable=False))
    op.drop_column('project', 'datasource')
    op.drop_column('project', 'external_id')
    # ### end Alembic commands ###