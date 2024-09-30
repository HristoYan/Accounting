from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.expense import Expense
from models.log_in import UserLog
from db.operations import add_money, withdraw_money
from app_config import db_path, fieldnames
import csv


def main():
    # if not log_in_path.exists():
    #     with open(log_in_path, 'w') as csv_file:
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames_log_in)
    #         writer.writeheader()
    logged = False
    while True:
        if logged:
            break

        print('Please Log in or Register (log/reg): ')
        log_reg = input()
        if log_reg == 'log':
            email = input('Email: ')
            password = input('Password: ')
            with open(log_in_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for user in reader:
                    if user['email'] == email and user['password'] == password: # noqa
                        logged = True
                        break
                else:
                    print('No such user was found!')

        elif log_reg == 'reg':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            age = input('Age: ')
            email = input('Email: ')
            password = input('Password: ')

            log_data = UserLog(first_name, last_name, age, email, password).to_dict()

            with open(log_in_path, 'a') as log_file:
                writer = csv.DictWriter(log_file, fieldnames=fieldnames_log_in)
                writer.writerow(log_data)
            print('Your registration was successful. Now you can Log In.')
        else:
            print('Invalid input!')

    if not db_path.exists():
        with open(db_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    print('Hello, welcome to your account manager')
    print('What would you like to do today?')

    while True:
        print('Choose one of the following options: add, extract, check: ')
        choice = input()
        if choice not in ['add', 'extract', 'check']:
            print('Invalid input. "add, extract and check" are the only valid commands.')

        if choice == 'add':
            add_money(log_data)

        elif choice == 'extract':
            withdraw_money()

        elif choice == 'check':
            pass


if __name__ == '__main__':
    main()

