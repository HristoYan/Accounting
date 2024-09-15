from pathlib import Path


db_path: Path = Path.cwd() / 'db/db.csv'
fieldnames: list = ['amount', 'time', 'category', 'type']
