"""change site models

Revision ID: 294b57e0c28
Revises: 135e1ae46fb
Create Date: 2015-01-24 23:12:10.024360

"""

# revision identifiers, used by Alembic.
revision = '294b57e0c28'
down_revision = '135e1ae46fb'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pages_ibfk_1', 'pages', type_='foreignkey')
    op.drop_column('pages', 'published')
    op.drop_column('pages', 'type')
    op.drop_column('pages', 'parent_id')
    op.drop_column('pages', 'url')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pages', sa.Column('url', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('pages', sa.Column('parent_id', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('pages', sa.Column('type', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('pages', sa.Column('published', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.create_foreign_key('pages_ibfk_1', 'pages', 'pages', ['parent_id'], ['id'])
    ### end Alembic commands ###
