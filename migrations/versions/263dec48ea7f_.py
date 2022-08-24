"""empty message

Revision ID: 263dec48ea7f
Revises: 
Create Date: 2022-08-23 12:23:44.461815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '263dec48ea7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('birth', sa.DateTime(), nullable=False),
    sa.Column('alergy_dai', sa.Integer(), nullable=True),
    sa.Column('alergy_cru', sa.Integer(), nullable=True),
    sa.Column('alergy_nut', sa.Integer(), nullable=True),
    sa.Column('alergy_pch', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###