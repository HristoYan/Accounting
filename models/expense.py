import time


class Expense:
    def __init__(self, spend_amount, type_of_expense: str, category: str):
        self.spend_amount = spend_amount
        self.category = category
        self.time = time.ctime()
        self.type_of_expense = type_of_expense

    def spend(self, user_data):
        if self.spend_amount > user_data.money:
            print(f'Impossible you don\'t have that much money!')
            return False

        else:
            user_data.money = -self.spend_amount
            print(f'You have ${user_data.money} left.')

    def to_dict(self):
        expense_info = {
            'spend_amount': self.spend_amount,
            'type_of_expense': self.type_of_expense,
            'category': self.category,
            'time': self.time,

        }
        return expense_info
