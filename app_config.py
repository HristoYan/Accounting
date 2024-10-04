from pathlib import Path


db_path: Path = Path.cwd() / 'db/db.csv'
fieldnames: list = ['user_id', 'amount', 'category', 'type', 'time']

log_in_path: Path = Path.cwd() / 'db/log.csv'
fieldnames_log_in: list = ['id', 'first_name', 'last_name', 'age', 'email', 'money', 'password']
