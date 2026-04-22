import sqlite3


class DBConnection:
    def __init__(self):
        self.con = sqlite3.connect("memory.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                embedding BLOB NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                importance INTEGER DEFAULT 1
            );
        """)

    def store_pickle(self, pickle):
        pass
