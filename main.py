#!/opt/homebrew/bin/python3

from db.schema import initialize_schema
from db.connection import get_connection

def insert_test_account():
  conn = get_connection()
  cur = conn.cursor()

  cur.execute(
    "INSERT INTO accounts (name, type, currency) VALUES (?, ?, ?)",
    ("Fidelity IRA", "brokerage", "USD")
  )

  conn.commit()
  conn.close()

def print_accounts():
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("SELECT * FROM accounts")
  rows = cur.fetchall()
  conn.close()

  print("Accounts:")
  for row in rows:
    print(row)

if __name__ == "__main__":
  initialize_schema()
  insert_test_account()
  print_accounts()
