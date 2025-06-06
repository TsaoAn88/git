"""Create users table

Revision ID: 80d61336db13
Revises: 20f8d2e67b18
Create Date: 2025-04-21 18:57:23.934944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80d61336db13'
down_revision: Union[str, None] = '20f8d2e67b18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    # ### end Alembic commands ###
