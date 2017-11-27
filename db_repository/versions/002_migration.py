from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
answer = Table('answer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('question_id', Integer),
    Column('answer_text', Text, nullable=False),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('survey_id', Integer),
    Column('question_type', String(length=64), nullable=False),
    Column('question_text', Text, nullable=False),
)

survey = Table('survey', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('survey_name', String(length=64), nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['answer'].create()
    post_meta.tables['question'].create()
    post_meta.tables['survey'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['answer'].drop()
    post_meta.tables['question'].drop()
    post_meta.tables['survey'].drop()
