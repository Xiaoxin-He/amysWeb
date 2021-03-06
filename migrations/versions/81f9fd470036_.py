"""empty message

Revision ID: 81f9fd470036
Revises: bab7707a8084
Create Date: 2020-11-29 23:45:37.118225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81f9fd470036'
down_revision = 'bab7707a8084'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('order_number', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.TEXT(), nullable=True),
    sa.Column('product_description', sa.TEXT(), nullable=True),
    sa.Column('product_image', sa.VARCHAR(length=20), nullable=False),
    sa.Column('product_price', sa.REAL(), nullable=True),
    sa.Column('users_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('order_number')
    )
    # ### end Alembic commands ###
