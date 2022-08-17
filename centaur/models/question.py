from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from centaur.db.base_class import Base


class Question(Base):
    id = Column(String, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    xqb_id = Column(Integer, nullable=False)
    raw_text = Column(ARRAY(String()), nullable=False)
    length = Column(Integer, nullable=False)
    tokens = Column(ARRAY(String()), nullable=False)
    avail_trans = Column(ARRAY(String()), nullable=False)
    translations = Column(JSONB)
    tournament = Column(String)
    meta = Column(JSONB)

    records = relationship('Record', order_by='Record.date', back_populates='question')
    caches = relationship('QantaCache', order_by='QantaCache.position', back_populates='question')
