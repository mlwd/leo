
import sqlite3
import sys
import os

def leo_db_connect():
  """Try to connect to sqlite3 data base file."""
  path_db = os.path.join(os.path.dirname(__file__), "leo_lookup.db");
  con = None
  try:
    con = sqlite3.connect(path_db)
  except:
    print("Data base file could not be opened.", file = sys.stderr)
  con.execute("create table if not exists dict (word_en, word_de, n int default 1)");
  return con

def leo_db_list():
  con = leo_db_connect()
  cur = con.cursor()
  word_list = cur.execute("select * from dict")
  con.commit()
  return word_list
