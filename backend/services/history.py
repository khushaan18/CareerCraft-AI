import sqlite3
from pathlib import Path
from datetime import datetime
DB=Path(__file__).resolve().parents[2]/"careercraft.db"
def init_db():
    with sqlite3.connect(DB) as c:c.execute("CREATE TABLE IF NOT EXISTS analyses(id INTEGER PRIMARY KEY,created_at TEXT,job_title TEXT,alignment_score INTEGER,payload TEXT)")
def save_analysis(x):
    init_db()
    with sqlite3.connect(DB) as c:c.execute("INSERT INTO analyses(created_at,job_title,alignment_score,payload) VALUES(?,?,?,?)",(datetime.utcnow().isoformat(),x.job.title,x.match.alignment_score,x.model_dump_json()))
def list_history():
    init_db()
    with sqlite3.connect(DB) as c: rows=c.execute("SELECT id,created_at,job_title,alignment_score FROM analyses ORDER BY id DESC LIMIT 20").fetchall()
    return [{"id":a,"created_at":b,"job_title":c,"alignment_score":d} for a,b,c,d in rows]
