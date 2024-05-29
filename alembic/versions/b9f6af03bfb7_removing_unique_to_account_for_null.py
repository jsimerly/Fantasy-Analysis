"""removing unique to account for null

Revision ID: b9f6af03bfb7
Revises: c41b71046f9f
Create Date: 2024-05-29 15:57:53.164431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9f6af03bfb7'
down_revision: Union[str, None] = 'c41b71046f9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('players_espn_id_key', 'players', type_='unique')
    op.drop_constraint('players_rotowire_id_key', 'players', type_='unique')
    op.drop_constraint('players_rotoworld_id_key', 'players', type_='unique')
    op.drop_constraint('players_sleeper_id_key', 'players', type_='unique')
    op.drop_constraint('players_swish_id_key', 'players', type_='unique')
    op.drop_constraint('players_yahoo_id_key', 'players', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('players_yahoo_id_key', 'players', ['yahoo_id'])
    op.create_unique_constraint('players_swish_id_key', 'players', ['swish_id'])
    op.create_unique_constraint('players_sleeper_id_key', 'players', ['sleeper_id'])
    op.create_unique_constraint('players_rotoworld_id_key', 'players', ['rotoworld_id'])
    op.create_unique_constraint('players_rotowire_id_key', 'players', ['rotowire_id'])
    op.create_unique_constraint('players_espn_id_key', 'players', ['espn_id'])
    # ### end Alembic commands ###
