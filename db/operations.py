import csv
import pendulum
from app_config import db_path, fieldnames
from models.expense import Expense
from models.log_in import UserLog


def add_money(log_data):
    print(type(log_data))
    money_to_add = int(input('How much money would you like to add: '))
    log_data.money = money_to_add

    print(log_data.money)


def withdraw_money():
    amount = float(input('How much: '))

    if amount < 100.0:
        expense_type = 'low'
    elif 100.0 > amount < 1000.0:
        expense_type = 'mid'
    else:
        expense_type = 'expensive'

    category = input('Category: ')

    expense1 = Expense(amount, expense_type, category)

    expense = expense1.spend()

    print(expense)
    