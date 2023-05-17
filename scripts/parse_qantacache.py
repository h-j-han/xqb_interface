import os, json
import pandas as pd
from centaur.config import settings
import pickle
from sqlalchemy import create_engine
import sqlalchemy
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

# file_path = os.path.join(os.getenv("MYHOME"), 'gits/xqb_interface/data/df4sql_xqb_initial_qantacache.pickle')
# file_path = os.path.join(os.getenv("MYHOME"), 'gits/xqb_interface/data/df4sql_xqbes_initial_qantacache_mod.pickle')
# file_path = os.path.join(os.getenv("MYHOME"), 'gits/xqb_interface/data/df4sql_xqb_feetthinking_qantacache.pickle')
file_path = os.path.join(os.getenv("MYHOME"), 'gits/xqb_interface/data/df4sql_xqb_prolific_qantacache.pickle')
with open(file_path, 'rb') as f:
    df = pickle.load(f)
# df['translations'] = list(map(lambda x: json.dumps(x), df['translations']))
# df['meta'] = list(map(lambda x: json.dumps(x), df['meta']))
df.to_sql('qantacache', con=engine, if_exists='append', index=False)
aa=0