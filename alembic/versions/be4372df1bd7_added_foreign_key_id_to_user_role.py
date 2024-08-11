"""added foreign key id to user role

Revision ID: be4372df1bd7
Revises: 050b9b082ab5
Create Date: 2024-08-11 11:43:41.208396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'be4372df1bd7'
down_revision: Union[str, None] = '050b9b082ab5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('account_type_id', sa.Integer(), nullable=False))
    op.drop_constraint('accounts_ibfk_1', 'accounts', type_='foreignkey')
    op.create_foreign_key(None, 'accounts', 'account_types', ['account_type_id'], ['id'])
    op.drop_column('accounts', 'account_type')
    op.add_column('business', sa.Column('account_type_id', sa.Integer(), nullable=False))
    op.drop_constraint('business_ibfk_1', 'business', type_='foreignkey')
    op.create_foreign_key(None, 'business', 'account_types', ['account_type_id'], ['id'])
    op.drop_column('business', 'account_type')
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', mysql.VARCHAR(length=45), nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.add_column('business', sa.Column('account_type', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'business', type_='foreignkey')
    op.create_foreign_key('business_ibfk_1', 'business', 'account_types', ['account_type'], ['id'])
    op.drop_column('business', 'account_type_id')
    op.add_column('accounts', sa.Column('account_type', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    op.create_foreign_key('accounts_ibfk_1', 'accounts', 'account_types', ['account_type'], ['id'])
    op.drop_column('accounts', 'account_type_id')
    # ### end Alembic commands ###
