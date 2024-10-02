import csv
import pendulum
from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.expense import Expense
from models.log_in import UserLog


def add_money(log_data):
    money_to_add = int(input('How much money would you like to add: '))
    log_data.money = money_to_add

    print(log_data.money)
    update_log(log_data)


def withdraw_money(log_data):
    amount = int(input('How much: '))

    if amount < 100:
        expense_type = 'low'
    elif 100 <= amount < 1000:
        expense_type = 'mid'
    else:
        expense_type = 'expensive'

    category = input('Category: ')

    expense1 = Expense(amount, expense_type, category)

    expense1.spend(log_data)
    expense_to_dict = expense1.to_dict()
    print(expense_to_dict)
    with open(db_path, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(expense_to_dict)
    update_log(log_data)


def update_log(log_data):
    print(log_data.to_dict())
    with open(log_in_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_log_in)
        writer.writeheader()
        writer.writerow(log_data.to_dict())
