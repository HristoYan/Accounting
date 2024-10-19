from app_config import db_path, fieldnames, log_in_path, fieldnames_log_in
from models.log_in import UserLog
from db.operations import add_money, withdraw_money, display_expenses
import csv
import sys
import re


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

        print('Please Log in or Register:\n1 - Log in\n2 - Register\n3 - Exit: ')
        log_reg = input()
        if log_reg not in ['1', '2', '3']:
            print('Invalid input. 1, 2, 3 are the only valid commands.')
            break

        if log_reg == '3':
            sys.exit()
        elif log_reg == '1':
            email = input('Email: ')
            password = input('Password: ')
            with open(log_in_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for user in reader:
                    if user['email'] == email and user['password'] == password: # noqa

                        user_data = UserLog(user['first_name'], # noqa
                                            user['last_name'], # noqa
                                            user['age'], # noqa
                                            user['email'], # noqa
                                            user['money'], # noqa
                                            user['password']) # noqa
                        # to make sure that the id is correct for it tries to change it to the next id available
                        user_data.id = user['id'] # noqa
                        logged = True
                        break
                else:
                    print('No such user was found!')

        elif log_reg == '2':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            age = int(input('Age: '))
            while True:
                flag = False
                try:
                    regexp = r'^[a-z]{2,}@[a-z]+\.[a-z]{2,3}$'
                    email = input('Email: ')

                    if re.fullmatch(regexp, email):
                        flag = True
                    else:
                        raise ValueError('Invalid Email Format!')
                except ValueError as e:
                    print(e)

                with open(log_in_path, 'r') as logFile:
                    reader = csv.DictReader(logFile)
                    for row in reader:
                        if row['email'] == email:  # noqa
                            print('The email already exist!')
                            flag = False
                            break
                if flag:
                    break

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

    print(f'Hello, {user_data.first_name} welcome to your account manager') # noqa
    print('What would you like to do today?')

    while True:
        print('Choose one of the following options: \n1 - add\n2 - expense\n3 - check\n4 - exit: ')

        choice = input()
        if choice not in ['1', '2', '3', '4']:
            print('Invalid input. 1, 2, 3, 4 are the only valid commands.')

        if choice == '1':
            add_money(user_data) # noqa

        elif choice == '2':
            withdraw_money(user_data)

        elif choice == '3':
            display_expenses(user_data)
        elif choice == '4':
            sys.exit()


if __name__ == '__main__':
    main()

