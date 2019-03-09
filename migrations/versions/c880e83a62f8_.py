"""empty message

Revision ID: c880e83a62f8
Revises: 814697ac04d4
Create Date: 2019-03-07 18:33:47.447797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c880e83a62f8'
down_revision = '814697ac04d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guild', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastVisited', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guild', schema=None) as batch_op:
        batch_op.drop_column('lastVisited')

    # ### end Alembic commands ###
