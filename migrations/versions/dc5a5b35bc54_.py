"""empty message

Revision ID: dc5a5b35bc54
Revises: c224ceb38450
Create Date: 2018-03-14 18:56:40.348355

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc5a5b35bc54'
down_revision = 'c224ceb38450'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=50), nullable=False),
                    sa.Column('body', sa.String(length=255), nullable=False),
                    sa.Column('postedby', sa.String(length=40), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
