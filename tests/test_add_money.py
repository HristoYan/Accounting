import unittest
from unittest.mock import patch, mock_open, MagicMock
from db.operations import add_money
from db.utilities import update_log
from app_config import log_in_path
import csv


class TestMoneyFunctions(unittest.TestCase):

    def setUp(self):
        # Mock user data
        self.user_data = MagicMock()
        self.user_data.id = 1
        self.user_data.money = 500  # Starting balance is 500

    @patch('builtins.input', return_value='200')
    @patch("builtins.open", new_callable=mock_open, read_data="id,money\n1,500\n2,1000\n")
    @patch("db.operations.update_log")
    def test_add_money_success(self, mock_update_log, mock_file, mock_input):
        # Simulate adding 200 units of money
        add_money(self.user_data)

        # Check if money has been updated correctly in the user data
        self.assertEqual(self.user_data.money, 700)  # 500 + 200 = 700

        # Verify that update_log was called to update the CSV
        mock_update_log.assert_called_once_with(self.user_data)

    @patch("builtins.open", new_callable=mock_open, read_data="id,money\n1,500\n2,1000\n")
    def test_update_log_success(self, mock_file):
        # Simulate calling update_log to modify the CSV file
        update_log(self.user_data)

        # Verify that the file was opened for reading, then for writing
        mock_file.assert_any_call(log_in_path, 'r')  # Check the reading mode

        mock_file.assert_any_call(log_in_path, 'w')  # Check the writing mode
        # Ensure the calls happened in the correct order
        # calls = [unittest.mock.call(log_in_path, 'r'), unittest.mock.call(log_in_path, 'w')]
        # mock_file.assert_has_calls(calls)
        # Verify that the money was updated in the file for the correct user
        handle = mock_file()
        handle.write.assert_called()  # Verifies that the file was written to

        # We can also assert the expected rows being written
        expected_calls = [
            unittest.mock.call().write('id,money\n'),
            unittest.mock.call().write('1,500\n'),  # Assuming 500 remains the same here
            unittest.mock.call().write('2,1000\n')
        ]
        handle.write.assert_has_calls(expected_calls, any_order=True)

    @patch('builtins.input', return_value='-100')
    @patch("builtins.open", new_callable=mock_open, read_data="id,money\n1,500\n2,1000\n")  # Mocking file in update_log
    def test_add_money_negative(self, mock_file, mock_input):
        # Adding negative money should not update the user's balance
        add_money(self.user_data)

        # Ensure money remains unchanged
        self.assertEqual(self.user_data.money, 500)  # Balance should not change

        # Ensure update_log was not called for invalid input
        mock_file().write.assert_not_called()  # No file write should happen


if __name__ == '__main__':
    unittest.main()
