import pendulum
import csv
from app_config import log_in_path, fieldnames_log_in


def update_log(user_data):
    updated_log = []
    with open(log_in_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if str(user_data.id) == str(row['id']): # noqa
                row['money'] = user_data.money # noqa

            updated_log.append(row)

    with open(log_in_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_log_in)
        writer.writeheader()
        writer.writerows(updated_log) # noqa


def display_all_expenses(user_id, rows):
    all_expenses = []
    for row in rows:
        if user_id == row['user_id']: # noqa
            all_expenses.append(row)

    return all_expenses


def display_by_date(user_id, rows):
    """Report expenditure for a specific date."""
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

    start, end = period_info()

    for row in rows:
        try:
            row_time = pendulum.parse(row['time']).timestamp()

            if user_id == row['user_id'] and start <= row_time <= end:
                period_expenses.append(row)
        except Exception as e:
            print(f"Error parsing date for: {row}, error: {e}")
            continue

    return period_expenses


def display_max_by_period(user_id, rows):
    period_expenses = [0]

    start, end = period_info()
    temp_amount = 0
    for row in rows:
        try:
            td = pendulum.parse(row['time']).timestamp()
            if user_id == row['user_id'] and start <= td <= end:
                if int(row['amount']) > temp_amount:
                    period_expenses[0] = row
                    temp_amount = int(row['amount'])
        except Exception as e:
            print(f"Error parsing date for: {row}, error: {e}")
    return period_expenses


def display_min_by_period(user_id, money, rows):
    period_expenses = [0]

    start, end = period_info()
    temp_amount = int(money)
    for row in rows:
        try:
            td = pendulum.parse(row['time']).timestamp()
            if user_id == row['user_id'] and start <= td <= end:
                if int(row['amount']) < temp_amount:
                    period_expenses[0] = row
                    temp_amount = int(row['amount'])
        except Exception as e:
            print(f"Error parsing date for: {row}, error: {e}")
    return period_expenses


def display_by_category(user_id, rows):
    category_expenses = []
    category = input('Category of expenses: ')
    for row in rows:
        if user_id == row['user_id'] and row['category'] == category:
            category_expenses.append(row)

    return category_expenses


def display_max_in_category(user_id, rows):
    max_category_list = []

    for row in rows:
        if user_id == row['user_id']:
            category = row['category']
            amount = row['amount']
            date = row['time']

            category_found = False
            for cat_dict in max_category_list:
                if cat_dict['category'] == category:
                    cat_dict['amount'] = max(cat_dict['amount'], amount)
                    category_found = True
                    break

            if not category_found:
                max_category_list.append({'category': category, 'amount': amount, 'time': date})

    return max_category_list


def display_min_in_category(user_id, rows):
    min_category_list = []

    for row in rows:
        if user_id == row['user_id']:
            category = row['category']
            amount = row['amount']
            date = row['time']

            category_found = False
            for cat_dict in min_category_list:
                if cat_dict['category'] == category:
                    cat_dict['amount'] = min(cat_dict['amount'], amount)
                    category_found = True
                    break

            if not category_found:
                min_category_list.append({'category': category, 'amount': amount, 'time': date})

    return min_category_list


def period_info():
    start_date = input('Starting from (YYYY-MM-DD): ')
    end_date = input('Ending on (YYYY-MM-DD): ')

    try:
        starting_date = pendulum.from_format(start_date, 'YYYY-MM-DD')
        finish_date = pendulum.from_format(end_date, 'YYYY-MM-DD').add(days=1)
    except ValueError:
        print('The dates should be in the correct format: YYYY-MM-DD.')
        return

    starting_timestamp = starting_date.timestamp()
    finish_timestamp = finish_date.timestamp()

    return starting_timestamp, finish_timestamp


def expense_view(expense):
    return f'${expense['amount']} spend on {expense['time']} for {expense['category']}'
