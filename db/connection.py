#!/opt/homebrew/bin/python3

import sqlite3
from pathlib import Path

DB_PATH = Path("portfolio.db")

def get_connection():
  return sqlite3.connect(DB_PATH)
