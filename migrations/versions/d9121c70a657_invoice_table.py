"""invoice table

Revision ID: d9121c70a657
Revises: 
Create Date: 2018-10-03 10:21:02.806369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9121c70a657'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_invoice_amount'), 'invoice', ['amount'], unique=False)
    op.create_index(op.f('ix_invoice_currency'), 'invoice', ['currency'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invoice_currency'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_amount'), table_name='invoice')
    op.drop_table('invoice')
    # ### end Alembic commands ###
