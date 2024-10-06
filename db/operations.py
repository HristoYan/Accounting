import csv
import pendulum
from db.utilities import (update_log, display_by_date, display_by_category, display_max_in_category,
                          display_min_in_category, display_by_period, display_all_expenses, expense_view,
                          display_max_by_period, display_min_by_period)
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

    expense1.spend(log_data)
    expense_to_dict = expense1.to_dict(log_data)
    with open(db_path, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(expense_to_dict)
    update_log(log_data)


def display_expenses(user_data):
    print('How would you like to see the expenses: all(all), by date(date), '
          'by period(period), max in period(max period), min in period(min period)'
          'by category(category), max in category(max), min in category(min)')
    sorting = input()
    expenses = []
    with open(db_path, 'r') as f:
        reader = csv.DictReader(f)

        if sorting == 'all':
            expenses = display_all_expenses(user_data.id, reader)

        elif sorting == 'date':
            expenses = display_by_date(user_data.id, reader)

        elif sorting == 'period':
            expenses = display_by_period(user_data.id, reader)

        elif sorting == 'max period':
            expenses = display_max_by_period(user_data.id, reader)
            print('The maximum expenditure in the given period: ')

        elif sorting == 'min period':
            expenses = display_min_by_period(user_data.id, user_data.money, reader)
            print('The minimum expenditure in the given period: ')

        elif sorting == 'category':
            expenses = display_by_category(user_data.id, reader)

        elif sorting == 'max':
            expenses = display_max_in_category(user_data.id, reader)
            print('The maximum expenditure in each category: ')

        elif sorting == 'min':
            expenses = display_min_in_category(user_data.id, user_data.money, reader)
            print('The minimum expenditure in each category: ')

    for expense in expenses:
        print(expense_view(expense))
