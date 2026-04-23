from pathlib import Path

db_path = Path("memory.db")

if db_path.exists():
    db_path.unlink()
