"""Initial8

Revision ID: c443789a1cb2
Revises: cc38000cd718
Create Date: 2021-02-28 09:24:29.739171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c443789a1cb2'
down_revision = 'cc38000cd718'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('children_wallet', sa.Column('parent_address', sa.String(length=34), nullable=False))
    op.create_foreign_key(None, 'children_wallet', 'parent_wallet', ['parent_address'], ['address'])
    op.create_unique_constraint(None, 'parent_wallet', ['address'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'parent_wallet', type_='unique')
    op.drop_constraint(None, 'children_wallet', type_='foreignkey')
    op.drop_column('children_wallet', 'parent_address')
    # ### end Alembic commands ###