"""photos

Revision ID: 8d4ee1677fb2
Revises: 75b2b926d295
Create Date: 2018-09-01 20:59:38.072793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d4ee1677fb2'
down_revision = '75b2b926d295'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pic', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'pic')
    # ### end Alembic commands ###