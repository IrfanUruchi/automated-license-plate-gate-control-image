import sqlite3, pathlib, datetime

DB_PATH = pathlib.Path('data/access.db')
DB_PATH.parent.mkdir(exist_ok=True)

# one global connection reused by the app
con = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS events(
                 id       INTEGER PRIMARY KEY AUTOINCREMENT,
                 ts       TEXT,          -- ISO-8601 timestamp
                 plate    TEXT,
                 verdict  TEXT           -- GRANTED / DENIED
               )""")
con.commit()

def log_event(plate: str, verdict: str):
    ts = datetime.datetime.now().isoformat(timespec='seconds')
    cur.execute("INSERT INTO events(ts,plate,verdict) VALUES (?,?,?)",
                (ts, plate.upper(), verdict.upper()))
    con.commit()
