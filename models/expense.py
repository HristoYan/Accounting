import pendulum


class Expense:
    def __init__(self, spend_amount: int, type_of_expense: str, category: str):
        self.spend_amount = spend_amount
        self.category = category
        self.time = pendulum.now('Europe/Sofia')
        self.type_of_expense = type_of_expense

    def spend(self, user_data):
        if self.spend_amount > user_data.money:
            print(f'Impossible you don\'t have that much money!')
            return False

        else:
            user_data.money = -self.spend_amount
            print(f'You have ${user_data.money} left.')
            return user_data.money

    def to_dict(self, user_data):
        expense_info = {
            'user_id': user_data.id,
            'amount': self.spend_amount,
            'type': self.type_of_expense,
            'category': self.category,
            'time': self.time,

        }
        return expense_info
