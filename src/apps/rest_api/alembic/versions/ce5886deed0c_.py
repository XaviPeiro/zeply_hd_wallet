"""empty message

Revision ID: ce5886deed0c
Revises: 
Create Date: 2023-08-13 16:31:14.238172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.encrypted.encrypted_type import StringEncryptedType

# revision identifiers, used by Alembic.
revision: str = 'ce5886deed0c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'master_key',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('master_key', StringEncryptedType(sa.String(255), b"zadfctf7_60grry167zrrrd67pevs0agoa2oasom1pg="), nullable=True),
    )

    op.create_table(
        'addresses',
        sa.Column('index', sa.Integer, nullable=False),
        sa.Column('address', sa.String, unique=True, nullable=False),
        sa.Column('private_key', sa.String, unique=True, nullable=False),  # TODO: Encrypt it
        sa.Column('master_key', sa.Integer, sa.ForeignKey('master_key.id')),
        sa.Column('coin', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('index', 'master_key'),
    )


def downgrade() -> None:
    pass
