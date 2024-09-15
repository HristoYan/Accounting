from app_config import db_path, fieldnames
from models.expense import Expense
from app_config import db_path, fieldnames
import csv


def main():

#     while True:
#         print('Please Log in or Register (log/reg): ')
#         log_reg = input()
#         if log_reg == 'log':
#             pass
#         elif log_reg == 'reg':
#             pass
#         else:
#             print('Invalid input!')

    if not db_path.exists():
        with open(db_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    print('Hello into your account manager')
    print('What would you like to do today?')

    while True:
        print('Choose one of the following options: add, extract, check: ')
        choice = input()
        if choice not in ['add', 'extract', 'check']:
            print('Invalid input. "add, extract and check" are the only valid commands.')

        if choice == 'add':
            pass

        elif choice == 'extract':
            pass

        elif choice == 'check':
            pass


if __name__ == '__main__':
    main()

