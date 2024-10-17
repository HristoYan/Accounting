import csv
from app_config import log_in_path


class UserLog:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, money: int, password: str):
        self.id = UserLog.get_next_id(log_in_path)
        self.email = email
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
        self._money = int(money)
        self._password = password

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        new_money = self._money + value
        self._money = new_money

    def to_dict(self):
        log_info = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'money': self._money,
            'password': self._password
        }
        return log_info

    @classmethod
    def get_next_id(cls, path_to_db):
        next_id = 1
        with open(path_to_db, 'r') as csv_db:
            reader = csv.DictReader(csv_db)
            for _ in reader:
                next_id += 1

        return next_id
