"""add site tables

Revision ID: 2c768d90bfb
Revises: 335d53bb657
Create Date: 2015-01-19 23:40:34.032201

"""

# revision identifiers, used by Alembic.
revision = '2c768d90bfb'
down_revision = '335d53bb657'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('version', sa.DateTime(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=120), nullable=True),
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('keywords', sa.String(length=255), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('static_pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['pages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('link_pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['pages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carousel_images',
    sa.Column('version', sa.DateTime(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=120), nullable=True),
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('path', sa.String(length=255), nullable=False),
    sa.Column('page_id', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['static_pages.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carousel_images')
    op.drop_table('link_pages')
    op.drop_table('static_pages')
    op.drop_table('pages')
    ### end Alembic commands ###