"""empty message

Revision ID: 742e0a6c2c06
Revises: 8a284baf731a
Create Date: 2016-04-12 22:20:50.602801

"""

# revision identifiers, used by Alembic.
revision = '742e0a6c2c06'
down_revision = '8a284baf731a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('completion', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'completion')
    ### end Alembic commands ###
