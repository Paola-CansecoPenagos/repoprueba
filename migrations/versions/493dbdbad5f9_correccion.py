"""correccion

Revision ID: 493dbdbad5f9
Revises: f456866134ff
Create Date: 2019-08-28 03:28:45.031778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493dbdbad5f9'
down_revision = 'f456866134ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('configuracion', sa.Column('cantidad_riego', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('configuracion', 'cantidad_riego')
    # ### end Alembic commands ###