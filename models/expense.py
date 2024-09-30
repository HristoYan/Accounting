import time


class Expense:
    def __init__(self, spend_amount, type_of_expense: str, category: str):
        self.spend_amount = spend_amount
        self.category = category
        self.time = time.ctime()
        self.type_of_expense = type_of_expense
        self._account_amount = 1000.00

    def get_account_amount(self):
        return self._account_amount

    def set_account_amount(self, amount, operation='add'):
        if operation == 'add':
            self._account_amount += amount
            print(f'You have added ${amount} to your account.')
        elif operation == 'subtract':
            self._account_amount -= amount
            print(f'You have spent ${amount}.')

        return f'You have ${self._account_amount} in your account.'

    def spend(self):
        if self.spend_amount > self._account_amount:
            print(f'Impossible you don\'t have that much money!')
            return False

        else:
            self.set_account_amount(self.spend_amount, 'subtract')
            print(f'You have ${self._account_amount} money left.')
            return self._account_amount
