"""create pages

Revision ID: 40cd0573744
Revises: 30108daf60
Create Date: 2015-01-24 23:38:23.119997

"""

# revision identifiers, used by Alembic.
revision = '40cd0573744'
down_revision = '30108daf60'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table
from datetime import datetime
from suittale.core import generate_uuid


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    sizes = table('pages',
                  sa.Column('version', sa.DateTime, onupdate=datetime.utcnow),
                  sa.Column('creation_date', sa.DateTime, default=datetime.utcnow),
                  sa.Column('updated_by', sa.String(120), nullable=True),
                  sa.Column('id', sa.String(255), primary_key=True, default=generate_uuid),
                  sa.Column('title', sa.String(5), nullable=False),
                  sa.Column('slug', sa.String(100)),
                  sa.Column('content_title', sa.String(100)),
                  sa.Column('content', sa.Text),
                  sa.Column('second_content_title', sa.String(100)),
                  sa.Column('second_content', sa.Text),
                  sa.Column('keywords', sa.String(255)))
    op.bulk_insert(sizes,
                   [
                       {'title': 'Acasa', 'slug': 'home'},
                       {'title': 'Despre', 'slug': 'about'},
                   ])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
