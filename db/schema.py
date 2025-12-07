#!/opt/homebrew/bin/python3

from .connection import get_connection

SCHEMA = """
CREATE TABLE IF NOT EXISTS accounts (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  currency TEXT NOT NULL
);
"""

def initialize_schema():
  conn = get_connection()
  cur = conn.cursor()
  cur.executescript(SCHEMA)
  conn.commit()
  conn.close()
