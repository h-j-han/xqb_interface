from centaur.db.session import SessionLocal
from centaur.models import Question, Player, Record, QantaCache, PlayerRoundStat
tournament_str = f'xqb_feetthinking'
db = SessionLocal()
questions = db.query(QantaCache).get(('xqb_feetthinking_round_01_question_0', 'bigwk9.tok.v1',10))
# questions = db.query(Question).filter(Question.tournament.startswith(tournament_str)).all()
print(questions[0].id)
print(questions[0].answer)
print(questions[0].xqb_id)
print(questions[0].raw_text)
print(questions[0].length)
print(questions[0].tokens)
print(questions[0].avail_trans)
print(questions[0].translations)
print(questions[0].tournament)
print(questions[0].meta)