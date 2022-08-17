from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from centaur.db.base_class import Base
from centaur.models import Question


class QantaCache(Base):
    question_id = Column(String, ForeignKey(Question.id), primary_key=True)
    trans_model = Column(String, primary_key=True)
    position = Column(Integer, primary_key=True)
    answer = Column(String, nullable=False)
    target_pos = Column(Integer)
    guesses = Column(ARRAY(String()))
    guess_scores = Column(ARRAY(Float()))
    buzz_scores = Column(ARRAY(Integer()))
    matches = Column(JSONB)
    text_highlight = Column(ARRAY(Integer()))
    matches_highlight = Column(JSONB)

    question = relationship("Question", back_populates="caches")
