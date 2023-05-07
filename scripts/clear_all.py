from centaur.models import Record, PlayerRoundStat, Player, Question, QantaCache
from centaur.db.session import SessionLocal

db = SessionLocal()
db.query(Record).delete()
db.commit()

db.query(PlayerRoundStat).delete()
db.commit()

db.query(Player).delete()
db.commit()


db.query(QantaCache).delete()
db.commit()
db.query(Question).delete()
db.commit()