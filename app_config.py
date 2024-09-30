from pathlib import Path


db_path: Path = Path.cwd() / 'db/db.csv'
fieldnames: list = ['amount', 'time', 'category', 'type']

log_in_path: Path = Path.cwd() / 'db/log.csv'
fieldnames_log_in: list = ['first_name', 'last_name', 'age', 'email', 'money', 'password']
