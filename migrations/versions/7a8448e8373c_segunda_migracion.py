"""segunda migracion

Revision ID: 7a8448e8373c
Revises: 7e5c01fe8257
Create Date: 2020-06-15 20:03:18.551077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8448e8373c'
down_revision = '7e5c01fe8257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_articles_timestamp'), 'articles', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_articles_timestamp'), table_name='articles')
    op.drop_column('articles', 'timestamp')
    # ### end Alembic commands ###
