import sqlite3
from memory import Memory
import pickle


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

    def store_memory(self, memory: Memory):
        # 1. Serialize the embedding vector into bytes (BLOB)
        embedding_blob = pickle.dumps(memory.embedding)

        # 2. Execute the INSERT statement using parameterized queries
        self.cur.execute(
            """
            INSERT INTO memories (content, embedding, importance)
            VALUES (?, ?, ?)
        """,
            (memory.content, embedding_blob, memory.importance),
        )

        # 3. Commit the transaction to save the changes to the file
        self.con.commit()


if __name__ == "__main__":
    # Example usage
    connection = DBConnection()

    memory = Memory(
        content="Query + response", embeddings=[1.2, 2.3, 3.4], importance=1
    )

    connection.store_memory(memory)
