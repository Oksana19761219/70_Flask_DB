"""changed name

Revision ID: a353cb9a5e12
Revises: 31fa8cdea418
Create Date: 2022-04-20 20:36:34.257125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a353cb9a5e12'
down_revision = '31fa8cdea418'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('city_name', sa.String(length=100), nullable=False))
    op.drop_column('cities', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('name', sa.VARCHAR(length=100), nullable=False))
    op.drop_column('cities', 'city_name')
    # ### end Alembic commands ###
