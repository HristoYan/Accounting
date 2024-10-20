import unittest
from unittest.mock import patch, mock_open, MagicMock
from db.operations import withdraw_money
import csv


class TestWithdrawMoney(unittest.TestCase):
    def setUp(self):
        self.log_data = MagicMock()
        self.log_data.id = 1
        self.log_data.first_name = 'John'
        self.log_data.last_name = 'Doe'
        self.log_data.age = 23
        self.log_data.email = 'john@doe.com'
        self.log_data.money = 500

    @patch('builtins.input', side_effect=['500', 'food'])  # Mock user input
    @patch('csv.DictWriter')  # Mock CSV DictWriter
    @patch('db.operations.Expense')  # Mock the Expense class
    @patch('db.operations.update_log')  # Mock update_log function
    @patch('db.operations.log_in_path', 'db/log.csv')  # Patch log_in_path
    @patch('db.operations.db_path', 'db/db.csv')  # Patch db_path
    @patch('builtins.open', new_callable=mock_open)  # Patch open
    def test_withdraw_money(self, mock_open, mock_db_path, mock_log_in_path, mock_update_log, mock_expense,
                            mock_csv_writer, mock_input):
        # Simulate different file handlers for each 'open' call
        mock_file1 = mock_open()  # First open (append to expense log)
        mock_file2 = mock_open()  # Second open (read log)
        mock_file3 = mock_open()  # Third open (write updated log)

        # Set side effect for different file operations
        mock_open.side_effect = [mock_file1, mock_file2, mock_file3]

        # Set up the mock Expense object
        mock_expense_instance = MagicMock()
        mock_expense.return_value = mock_expense_instance
        mock_expense_instance.to_dict.return_value = {'amount': 500, 'type': 'mid', 'category': 'food'}

        # Call the function
        withdraw_money(self.log_data)

        # Assert input() was called with expected prompts
        mock_input.assert_any_call('How much: ')
        mock_input.assert_any_call('Category: ')

        # Assert the Expense object was instantiated correctly
        mock_expense.assert_called_once_with(500, 'mid', 'food')

        # Assert the spend method was called
        mock_expense_instance.spend.assert_called_once_with(self.log_data)

        # Assert to_dict method was called
        mock_expense_instance.to_dict.assert_called_once_with(self.log_data)

        # Print all open() call arguments to debug
        print(f"mock_open call args list: {mock_open.call_args_list}")

        # Check if open() was called three times now
        self.assertEqual(mock_open.call_count, 3)

        # Ensure each file was opened correctly
        mock_open.assert_any_call('db/db.csv', 'a')  # First call: for appending the expense
        mock_open.assert_any_call('db/log.csv', 'r')  # Second call: reading log file
        mock_open.assert_any_call('db/log.csv', 'w')  # Third call: writing updated log

        # Ensure DictWriter was called twice
        self.assertEqual(mock_csv_writer.call_count, 2)

        # Check the first call to DictWriter (for the expense)
        call1 = mock_csv_writer.call_args_list[0]
        self.assertEqual(call1[1]['fieldnames'], ['user_id', 'amount', 'category', 'type', 'time'])

        # Check the second call to DictWriter (for updating the log)
        call2 = mock_csv_writer.call_args_list[1]
        self.assertEqual(call2[1]['fieldnames'], ['id', 'first_name', 'last_name', 'age', 'email', 'money', 'password'])

        # Ensure the log is updated
        mock_update_log.assert_called_once_with(self.log_data)


if __name__ == '__main__':
    unittest.main()
