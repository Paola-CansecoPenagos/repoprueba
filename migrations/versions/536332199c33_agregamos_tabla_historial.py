"""agregamos tabla Historial

Revision ID: 536332199c33
Revises: 4f59d0943413
Create Date: 2019-08-23 02:26:41.500082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536332199c33'
down_revision = '4f59d0943413'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historial',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario', sa.String(), nullable=True),
    sa.Column('nombre_conf', sa.String(), nullable=True),
    sa.Column('fecha_hora', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historial')
    # ### end Alembic commands ###