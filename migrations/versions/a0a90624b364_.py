"""empty message

Revision ID: a0a90624b364
Revises: c5c12655125b
Create Date: 2020-11-24 16:36:50.807966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0a90624b364'
down_revision = 'c5c12655125b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_description', table_name='products')
    op.drop_index('ix_products_product_kind', table_name='products')
    op.drop_index('ix_products_product_name', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('description', sa.VARCHAR(length=128), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('product_kind', sa.VARCHAR(length=128), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_products_product_name', 'products', ['product_name'], unique=False)
    op.create_index('ix_products_product_kind', 'products', ['product_kind'], unique=False)
    op.create_index('ix_products_description', 'products', ['description'], unique=False)
    # ### end Alembic commands ###
