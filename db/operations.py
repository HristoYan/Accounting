import csv
from db.utilities import (update_log, display_by_date, display_by_category, display_max_in_category,
                          display_min_in_category, display_by_period, display_all_expenses, expense_view,
                          display_max_by_period, display_min_by_period)
from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.expense import Expense


def add_money(log_data):
    print(log_data.money)
    money_to_add = int(input('How much money would you like to add: '))
    if money_to_add <= 0:
        print("Invalid amount. You cannot add a negative amount of money.")
        return

    log_data.money = money_to_add

    update_log(log_data)
    return log_data.money


def withdraw_money(log_data):
    amount = int(input('How much: '))
    if amount < 0:
        print('The expense must be a positive number!')
        return

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
    print('How would you like to see the expenses: \n1 - all\n2 - by date'
          '\n3 - by period\n4 - max in period\n5 - min in period'
          '\n6 - by category\n7 - max in category\n8 - min in category')
    sorting = input()
    if sorting not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print('Invalid input. 1, 2, 3, 4, 5, 6, 7, 8 are the only valid commands.')

    expenses = []
    with open(db_path, 'r') as f:
        reader = csv.DictReader(f)

        if sorting == '1':
            expenses = display_all_expenses(user_data.id, reader)

        elif sorting == '2':
            expenses = display_by_date(user_data.id, reader)

        elif sorting == '3':
            expenses = display_by_period(user_data.id, reader)

        elif sorting == '4':
            expenses = display_max_by_period(user_data.id, reader)
            print('The maximum expenditure in the given period: ')

        elif sorting == '5':
            expenses = display_min_by_period(user_data.id, user_data.money, reader)
            print('The minimum expenditure in the given period: ')

        elif sorting == '6':
            expenses = display_by_category(user_data.id, reader)

        elif sorting == '7':
            expenses = display_max_in_category(user_data.id, reader)
            print('The maximum expenditure in each category: ')

        elif sorting == '8':
            expenses = display_min_in_category(user_data.id, reader)
            print('The minimum expenditure in each category: ')

    for expense in expenses:
        print(expense_view(expense))
