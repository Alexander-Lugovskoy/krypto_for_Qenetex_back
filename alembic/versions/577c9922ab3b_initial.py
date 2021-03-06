"""Initial

Revision ID: 577c9922ab3b
Revises: 1ec01acf440f
Create Date: 2021-02-27 14:37:55.956684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '577c9922ab3b'
down_revision = '1ec01acf440f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='data_pkey')
    )
    # ### end Alembic commands ###
