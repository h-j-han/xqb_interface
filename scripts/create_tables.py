from sqlalchemy import Column, ForeignKey, Integer, Float, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy import Table, MetaData

from centaur.models import Player, Question
from centaur.db.session import engine

meta = MetaData()


Table(
    'question', meta,
    Column('id', String, primary_key=True, index=True),
    Column('xqb_id', Integer, nullable=False),
    Column('answer', String, nullable=False),
    Column('raw_text', ARRAY(String()), nullable=False),
    Column('length', Integer, nullable=False),
    Column('tokens', ARRAY(String()), nullable=False),
    Column('avail_trans', ARRAY(String()), nullable=False),
    Column('translations', JSONB),
    Column('tournament', String),
    Column('meta', JSONB),
)

Table(
    'player', meta,
    Column('id', String, primary_key=True, index=True),
    Column('ip_addr', String, index=True),
    Column('name', String),
    Column('email', String),
    Column('llevel', String),
    Column('mediator_name', String),
    Column('score', Integer),
    Column('questions_seen', JSONB),
    Column('questions_answered', JSONB),
    Column('questions_correct', JSONB),
)

Table(
    'features', meta,
    Column('id', String, ForeignKey(Player.id, ondelete="CASCADE"), primary_key=True, index=True),
    Column('enabled_explanation', JSONB),
    Column('enabled_config', JSONB),
    Column('n_seen', Integer),
    Column('n_answered', Integer),
    Column('n_correct', Integer),
    Column('n_seen_by_explanation', JSONB),
    Column('n_seen_by_config', JSONB),
    Column('n_answered_by_explanation', JSONB),
    Column('n_answered_by_config', JSONB),
    Column('n_correct_by_explanation', JSONB),
    Column('n_correct_by_config', JSONB),
)

Table(
    'qantacache', meta,
    Column('question_id', String, ForeignKey(Question.id), primary_key=True),
    Column('trans_model', String, primary_key=True),
    Column('position', Integer, primary_key=True),
    Column('answer', String, nullable=False),
    Column('target_pos', Integer),
    Column('guesses', ARRAY(String())),
    Column('guess_scores', ARRAY(Float())),
    Column('buzz_scores', ARRAY(Integer())),
    Column('matches', JSONB),
    Column('text_highlight', ARRAY(Integer())),
    Column('matches_highlight', JSONB),
)


Table(
    'record', meta,
    Column('id', String, primary_key=True, index=True),
    Column('player_id', String, ForeignKey(Player.id), nullable=False, index=True),
    Column('question_id', String, ForeignKey(Question.id), nullable=False, index=True),
    Column('position_start', Integer, nullable=False),
    Column('position_buzz', Integer, nullable=False),
    Column('guess', String),
    Column('result', Integer),
    Column('qb_score', Integer),
    Column('ew_score', Float),
    Column('explanation_config', String),
    Column('translation_type', String),
    Column('mediator_name', String),
    Column('room_id', String),
    Column('player_list', JSONB),
    Column('date', TIMESTAMP(timezone=True)),
)

Table(
    'playerroundstat', meta,
    Column('player_id', String, ForeignKey(Player.id), primary_key=True, nullable=False, index=True),
    Column('room_id', String, primary_key=True, nullable=False, index=True),
    Column('qb_score', Integer),
    Column('ew_score', Float),
    Column('questions_answered', JSONB),
    Column('questions_correct', JSONB),
)

meta.create_all(engine)
