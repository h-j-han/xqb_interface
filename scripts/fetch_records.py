import os
import json
import altair as alt
import pandas as pd
from centaur.db.session import SessionLocal
from centaur.models import Record, Player
from centaur.utils import EXPLANATIONS, ID_TO_CONFIG


session = SessionLocal()