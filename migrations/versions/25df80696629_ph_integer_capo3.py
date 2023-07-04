"""ph integer capo3

Revision ID: 25df80696629
Revises: 3f4ec3347e31
Create Date: 2019-10-09 03:01:33.223919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25df80696629'
down_revision = '3f4ec3347e31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('configuracion', 'ph_min')
    op.drop_column('configuracion', 'ph_max')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('configuracion', sa.Column('ph_max', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('configuracion', sa.Column('ph_min', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###