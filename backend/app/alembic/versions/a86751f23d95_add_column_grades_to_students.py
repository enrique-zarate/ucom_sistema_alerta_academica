"""Add column grades to students

Revision ID: a86751f23d95
Revises: 23c91477e74f
Create Date: 2023-12-21 03:52:25.519475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a86751f23d95'
down_revision = '23c91477e74f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # grades = relationship("Grade", back_populates="student")
    op.add_column('student', sa.Column('grades', sa.ARRAY(sa.INTEGER()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'grades')
    # ### end Alembic commands ###
