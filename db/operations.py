import csv
import pendulum
from app_config import db_path, fieldnames
from models.expense import Expense


def add_money(amount):
    print(Expense.set_account_amount(amount, operation='add'))


def withdraw_money(amount):
    print(Expense.set_account_amount(amount, operation='subtract'))
    