# import unittest
# from unittest.mock import patch, mock_open, MagicMock
# from db.operations import withdraw_money
# import csv
#
#
# class TestWithdrawMoney(unittest.TestCase):
#     def setUp(self):
#         self.log_data = MagicMock()
#         self.log_data.id = 1
#         self.log_data.first_name = 'John'
#         self.log_data.last_name = 'Doe'
#         self.log_data.age = 23
#         self.log_data.email = 'john@doe.com'
#         self.log_data.money = 500
#
#     @patch('builtins.input', side_effect=['500', 'food'])
#     @patch('csv.DictWriter')
#     @patch('db.operations.Expense')
#     @patch('db.operations.update_log')
#     @patch('db.operations.log_in_path', 'db/log.csv')
#     @patch('db.operations.db_path', 'db/db.csv')
#     @patch('builtins.open', new_callable=mock_open)
#     def test_withdraw_money(self, mock_open, mock_db_path, mock_log_in_path, mock_update_log,
#                             mock_expense, mock_csv_writer, mock_input):
#         # Debugging print statements to confirm mock order
#         print(f"mock_open: {mock_open}")
#         print(f"mock_db_path: {mock_db_path}")
#         print(f"mock_log_in_path: {mock_log_in_path}")
#         print(f"mock_update_log: {mock_update_log}")
#         print(f"mock_expense: {mock_expense}")
#         print(f"mock_csv_writer: {mock_csv_writer}")
#         print(f"mock_input: {mock_input}")
#
#         # Create mock file handles
#         mock_file1 = mock_open()
#         mock_file2 = mock_open()
#         mock_file3 = mock_open()
#
#         # Setting the sequence of mock_open calls
#         mock_open.side_effect = [mock_file1, mock_file2, mock_file3]
#
#         # Mocking the Expense object and its methods
#         mock_expense_instance = MagicMock()
#         mock_expense.return_value = mock_expense_instance
#         mock_expense_instance.to_dict.return_value = {'amount': 500, 'type': 'mid', 'category': 'food'}
#
#         # Call the withdraw_money function
#         withdraw_money(self.log_data)
#
#         # Verify input calls
#         mock_input.assert_any_call('How much: ')
#         mock_input.assert_any_call('Category: ')
#
#         # Check if the Expense object was created and spend was called
#         mock_expense.assert_called_once_with(500, 'mid', 'food')
#         mock_expense_instance.spend.assert_called_once_with(self.log_data)
#         mock_expense_instance.to_dict.assert_called_once_with(self.log_data)
#
#         # Verify the number of times open() was called
#         self.assertEqual(mock_open.call_count, 3)
#         mock_open.assert_any_call(mock_db_path, 'a')  # For appending expense
#         mock_open.assert_any_call(mock_log_in_path, 'r')  # For reading log
#         mock_open.assert_any_call(mock_log_in_path, 'w')  # For writing updated log
#
#         # Verify the CSV writer call count and fieldnames
#         self.assertEqual(mock_csv_writer.call_count, 2)
#         call1 = mock_csv_writer.call_args_list[0]
#         self.assertEqual(call1[1]['fieldnames'], ['user_id', 'amount', 'category', 'type', 'time'])
#
#         call2 = mock_csv_writer.call_args_list[1]
#         self.assertEqual(call2[1]['fieldnames'], ['id', 'first_name', 'last_name', 'age', 'email', 'money', 'password'])
#
#         # Check if the update_log function was called
#         mock_update_log.assert_called_once_with(self.log_data)
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.mock import patch, mock_open, MagicMock
from db.operations import withdraw_money


import unittest
from unittest.mock import patch, mock_open, MagicMock
from db.operations import withdraw_money


class TestWithdrawMoney(unittest.TestCase):
    def setUp(self):
        self.log_data = MagicMock()
        self.log_data.id = 1
        self.log_data.first_name = 'John'
        self.log_data.last_name = 'Doe'
        self.log_data.age = 23
        self.log_data.email = 'john@doe.com'
        self.log_data.money = 500

    @patch('db.operations.input', side_effect=['500', 'food'])  # Patch input from where it's used
    @patch('db.operations.csv.DictWriter')  # Patch DictWriter from where it's used
    @patch('builtins.open', new_callable=mock_open)  # Patch builtins.open
    @patch('db.operations.db_path', 'mock/db.csv')  # Mock the db_path so it doesn't point to a real file
    @patch('db.operations.log_in_path', 'mock/log.csv')  # Mock the log_in_path
    def test_withdraw_money(self, mock_open, mock_db_path, mock_log_in_path, mock_csv_writer, mock_input):
        print(f"mock_csv_writer: {mock_csv_writer}")
        print(f"mock_input: {mock_input}")
        print(f"mock_db_path: {mock_db_path}")
        print(f"mock_log_in_path: {mock_log_in_path}")

        # Call the withdraw_money function
        withdraw_money(self.log_data)

        # Verify that the open function was called with the mocked paths
        mock_open.assert_any_call('mock/db.csv', 'a')
        mock_open.assert_any_call('mock/log.csv', 'r')
        mock_open.assert_any_call('mock/log.csv', 'w')


if __name__ == '__main__':
    unittest.main()
