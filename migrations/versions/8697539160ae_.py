"""empty message

Revision ID: 8697539160ae
Revises: 
Create Date: 2021-04-14 09:00:15.711006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8697539160ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_firstname', sa.String(length=100), nullable=True),
    sa.Column('client_lastname', sa.String(length=100), nullable=True),
    sa.Column('client_username', sa.String(length=100), nullable=True),
    sa.Column('client_email', sa.String(length=100), nullable=True),
    sa.Column('client_password', sa.String(length=100), nullable=True),
    sa.Column('client_birthday', sa.String(length=100), nullable=True),
    sa.Column('client_gender', sa.String(length=100), nullable=True),
    sa.Column('client_nationality', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
