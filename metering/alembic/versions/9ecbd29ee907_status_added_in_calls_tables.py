"""status added in calls tables

Revision ID: 9ecbd29ee907
Revises: eeec29a1af7b
Create Date: 2019-08-12 15:13:51.507698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ecbd29ee907'
down_revision = 'eeec29a1af7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usage_table', sa.Column(
        'status', sa.VARCHAR(length=225), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usage_table', 'status')
    # ### end Alembic commands ###
