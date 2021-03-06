"""empty message

Revision ID: 2ca90ee6635
Revises: 4db3ec23f2e
Create Date: 2015-03-05 05:45:47.142509

"""

# revision identifiers, used by Alembic.
revision = '2ca90ee6635'
down_revision = '4db3ec23f2e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('second_name', sa.String(length=64), nullable=True),
    sa.Column('third_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('birth_day', sa.DateTime(), nullable=True),
    sa.Column('death_day', sa.DateTime(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_last_name'), 'authors', ['last_name'], unique=False)
    op.create_table('publications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('annotation', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publications_title'), 'publications', ['title'], unique=False)
    op.create_table('authorship',
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['publication_id'], ['publications.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authorship')
    op.drop_index(op.f('ix_publications_title'), table_name='publications')
    op.drop_table('publications')
    op.drop_index(op.f('ix_authors_last_name'), table_name='authors')
    op.drop_table('authors')
    ### end Alembic commands ###
