import pendulum
import csv
from app_config import log_in_path, fieldnames_log_in


def update_log(user_data):
    updated_log = []
    with open(log_in_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'User data id: {user_data.id}')
            print(f"Row id: {row['id']}") # noqa
            if str(user_data.id) == str(row['id']): # noqa

                row['money'] = user_data.money

            updated_log.append(row)

    with open(log_in_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_log_in)
        writer.writeheader()
        for row in updated_log:
            print(row)
            writer.writerow(row) # noqa


def display_all_expenses(user_id, rows):
    all_expenses = []
    for row in rows:
        if user_id == row['user_id']: # noqa
            all_expenses.append(row)

    return all_expenses


def display_by_date(user_id, rows):

    date_expenses = []
    date_to_check = input('Date to check(YYYY-MM-DD): ')
    try:
        date_to_check = pendulum.from_format(date_to_check, 'YYYY-MM-DD').date()
    except ValueError:
        print('The date should be in the correct format: YYYY-MM-DD.')
        return

    dtc = pendulum.parse(str(date_to_check))
    dtc_str = f'{dtc.year}-{dtc.month}-{dtc.day}'

    for row in rows:
        dt = pendulum.parse(row['time'], struct=False)
        row_year, row_month, row_day = dt.year, dt.month, dt.day
        row_date = f'{row_year}-{row_month}-{row_day}'
        if user_id == row['user_id'] and dtc_str == row_date:  # noqa
            date_expenses.append(row)

    return date_expenses


def display_by_period(user_id, rows):
    period_expenses = []
    starting_date = input('Starting from(YYYY-MM-DD): ')
    finish_date = input('Ending on(YYYY-MM-DD): ')
    try:
        starting_date = pendulum.from_format(starting_date, 'YYYY-MM-DD').date()
        finish_date = pendulum.from_format(finish_date, 'YYYY-MM-DD').date()
    except ValueError:
        print('The dates should be in the correct format: YYYY-MM-DD.')
        return

    starting_date = pendulum.parse(str(starting_date)).timestamp()
    finish_date = finish_date.add(days=1)
    finish_date = pendulum.parse(str(finish_date)).timestamp()

    for row in rows:
        td = pendulum.parse(row['time'], struct=False).timestamp()
        if user_id == row['user_id'] and starting_date <= td <= finish_date:
            period_expenses.append(row)

    return period_expenses


def display_by_category(user_id, rows):
    category_expenses = []
    category = input('Category of expenses: ')
    for row in rows:
        if user_id == row['user_id'] and row['category'] == category:
            category_expenses.append(row)

    return category_expenses


def display_max_in_category(user_id, rows):
    category_expenses = [0]
    expense_amount = 0
    category = input('Category of expenses: ')
    for row in rows:
        if user_id == row['user_id'] and row['category'] == category:
            if int(row['amount']) > expense_amount:
                expense_amount = int(row['amount'])
                category_expenses[0] = row

    return category_expenses


def display_min_in_category(user_id, user_money, rows):
    category_expenses = [0]
    expense_amount = user_money
    category = input('Category of expenses: ')
    for row in rows:
        if user_id == row['user_id'] and row['category'] == category:
            if int(row['amount']) < expense_amount:
                expense_amount = int(row['amount'])
                category_expenses[0] = row

    return category_expenses


def expense_view(expense):
    return f'${expense['amount']} spend on {expense['time']} for {expense['category']}'
