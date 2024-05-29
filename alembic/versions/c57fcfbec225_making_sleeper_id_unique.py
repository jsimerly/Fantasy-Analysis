"""making sleeper_id unique

Revision ID: c57fcfbec225
Revises: 4d21d3e24432
Create Date: 2024-05-29 15:30:25.318710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c57fcfbec225'
down_revision: Union[str, None] = '4d21d3e24432'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'players', ['sleeper_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'players', type_='unique')
    # ### end Alembic commands ###
