"""got rid of role table

Revision ID: bc474b4ee7b7
Revises: adf5b5c442c4
Create Date: 2024-08-16 14:08:59.495961

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "bc474b4ee7b7"
down_revision: Union[str, None] = "adf5b5c442c4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "business_users", sa.Column("role_name", sa.String(length=45), nullable=False)
    )
    op.drop_column("business_users", "role_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "business_users",
        sa.Column("role_id", mysql.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("business_users", "role_name")
    # ### end Alembic commands ###
