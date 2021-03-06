"""products table

Revision ID: fb9676912bb5
Revises: eab650e2e74a
Create Date: 2020-11-23 13:00:19.590039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb9676912bb5'
down_revision = 'eab650e2e74a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('product_kind', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id', 'price')
    )
    op.create_index(op.f('ix_products_description'), 'products', ['description'], unique=True)
    op.create_index(op.f('ix_products_product_kind'), 'products', ['product_kind'], unique=True)
    op.create_index(op.f('ix_products_product_name'), 'products', ['product_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_product_name'), table_name='products')
    op.drop_index(op.f('ix_products_product_kind'), table_name='products')
    op.drop_index(op.f('ix_products_description'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
