"""change name once more

Revision ID: dc0d14c65fd3
Revises: fdfcaf2abbab
Create Date: 2022-04-20 20:57:07.152985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0d14c65fd3'
down_revision = 'fdfcaf2abbab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city_name', sa.String(length=100), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('city_name')

    # ### end Alembic commands ###