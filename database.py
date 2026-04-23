import sqlite3
from memory import Memory
import pickle


class DBConnection:
    def __init__(self):
        self.con = sqlite3.connect("memory.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                embedding BLOB NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                importance INTEGER DEFAULT 1
            );
        """)

    def retrieve_all_memories(self):
        # 1. Fetch ALL rows from the database
        self.cur.execute("SELECT id, content, embedding, importance FROM memories")
        rows = self.cur.fetchall()

        all_memories = []

        # 2. Iterate through and deserialize the embeddings
        for row in rows:
            mem_id, content, embedding_blob, importance = row

            # Deserialize the BLOB back into a Python list of floats
            mem_vector = pickle.loads(embedding_blob)

            all_memories.append(
                {
                    "id": mem_id,
                    "content": content,
                    "embedding": mem_vector,
                    "importance": importance,
                }
            )

        return all_memories

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

    memory = Memory(content="Query + response", embedding=[1.2, 2.3, 3.4], importance=1)

    connection.store_memory(memory)

    memories = connection.retrieve_all_memories()

    print(memories)
