from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.log_in import UserLog
from db.operations import add_money, withdraw_money
import csv
import sys


def main():
    user_data = {}
    if not log_in_path.exists():
        with open(log_in_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames_log_in)
            writer.writeheader()

    logged = False
    while True:
        if logged:
            break

        print('Please Log in or Register (log/reg/exit): ')
        log_reg = input()
        if log_reg == 'exit':
            sys.exit()
        elif log_reg == 'log':
            email = input('Email: ')
            password = input('Password: ')
            with open(log_in_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for user in reader:
                    if user['email'] == email and user['password'] == password: # noqa

                        name = user['first_name'] # noqa

                        user_data = UserLog(user['first_name'], user['last_name'], user['age'], user['email'], # noqa
                                            user['money'], user['password']) # noqa
                        print(f'Log in id: {user['id']}')
                        user_data.id = user['id']
                        print(f'Log in id: {user_data.id}')
                        logged = True
                        break
                else:
                    print('No such user was found!')

        elif log_reg == 'reg':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            age = int(input('Age: '))
            email = input('Email: ')
            money = int(input('How much money do you have: '))
            password = input('Password: ')

            user_data = UserLog(first_name, last_name, age, email, money, password).to_dict()

            with open(log_in_path, 'a', newline='') as log_file:
                writer = csv.DictWriter(log_file, fieldnames=fieldnames_log_in)
                writer.writerow(user_data)
            print('Your registration was successful. Now you can Log In.')
        else:
            print('Invalid input!')

    if not db_path.exists():
        with open(db_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    print(f'Hello, {name} welcome to your account manager') # noqa
    print(f'Main extract id: {user_data.id}')
    print('What would you like to do today?')

    while True:
        print('Choose one of the following options: add, extract, check: ')
        choice = input()
        if choice not in ['add', 'extract', 'check']:
            print('Invalid input. "add, extract and check" are the only valid commands.')

        if choice == 'add':
            add_money(user_data) # noqa

        elif choice == 'extract':
            print(f'Main extract id: {user_data.id}')
            withdraw_money(user_data)

        elif choice == 'check':
            pass


if __name__ == '__main__':
    main()

