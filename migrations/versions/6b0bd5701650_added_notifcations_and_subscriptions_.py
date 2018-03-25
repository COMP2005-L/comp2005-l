"""Added Notifcations and Subscriptions tables

Revision ID: 6b0bd5701650
Revises: 96c767a93183
Create Date: 2018-03-25 15:24:53.035537

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6b0bd5701650'
down_revision = '96c767a93183'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('discussion_group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discussion_group',
                    sa.Column('discussionid', sa.INTEGER(), nullable=False),
                    sa.Column('discussiontitle', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('discussionbody', sa.VARCHAR(length=255), nullable=False),
                    sa.Column('discussiondateposted', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('discussionposter_id', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['discussionposter_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('discussionid')
                    )
    # ### end Alembic commands ###