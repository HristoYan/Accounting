import csv
import pendulum
from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.expense import Expense
from models.log_in import UserLog


def add_money(log_data):
    print(f'Add money id: {log_data.id}')
    money_to_add = int(input('How much money would you like to add: '))
    log_data.money = money_to_add

    print(log_data.money)
    update_log(log_data)


def withdraw_money(log_data):
    amount = int(input('How much: '))
    print(f'Withdraw id: {log_data.id}')
    if amount < 100:
        expense_type = 'low'
    elif 100 <= amount < 1000:
        expense_type = 'mid'
    else:
        expense_type = 'expensive'

    category = input('Category: ')

    expense1 = Expense(amount, expense_type, category)

    user_money = expense1.spend(log_data)
    expense_to_dict = expense1.to_dict(log_data)
    with open(db_path, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(expense_to_dict)
    update_log(log_data, user_money)


def update_log(user_data):
    updated_log = []
    with open(log_in_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'User data id: {user_data.id}')
            print(f"Row id: {row['id']}")
            if str(user_data.id) == str(row['id']): # noqa

                row['money'] = user_data.money

            updated_log.append(row)

    with open(log_in_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_log_in)
        writer.writeheader()
        for row in updated_log:
            print(row)
            writer.writerow(row)
