"""empty message

Revision ID: 142812d6663e
Revises: 89e1dab5c281
Create Date: 2019-04-30 16:25:13.579739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '142812d6663e'
down_revision = '89e1dab5c281'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guild', schema=None) as batch_op:
        batch_op.alter_column('rockbiteId',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
        batch_op.create_unique_constraint(batch_op.f('uq_guild_rockbiteId'), ['rockbiteId'])

    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.alter_column('rockbiteId',
               existing_type=sa.VARCHAR(length=24),
               nullable=True)
        batch_op.create_unique_constraint(batch_op.f('uq_player_rockbiteId'), ['rockbiteId'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_player_rockbiteId'), type_='unique')
        batch_op.alter_column('rockbiteId',
               existing_type=sa.VARCHAR(length=24),
               nullable=True)

    with op.batch_alter_table('guild', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_guild_rockbiteId'), type_='unique')
        batch_op.alter_column('rockbiteId',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)

    # ### end Alembic commands ###
