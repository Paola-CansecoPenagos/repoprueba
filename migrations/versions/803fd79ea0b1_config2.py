"""config2

Revision ID: 803fd79ea0b1
Revises: 272d87762b00
Create Date: 2019-11-23 23:45:31.925007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '803fd79ea0b1'
down_revision = '272d87762b00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('configuracion', 'inicio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('configuracion', sa.Column('inicio', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
