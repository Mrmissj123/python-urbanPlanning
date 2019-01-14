"""initial migration

Revision ID: 538119d3e42a
Revises: 
Create Date: 2018-02-06 21:41:57.849650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538119d3e42a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('imagesinfodf', 'migrate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('imagesinfodf', sa.Column('migrate', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
