import unittest
from unittest.mock import patch, mock_open, MagicMock
from db.operations import add_money
from db.utilities import update_log
from app_config import log_in_path
import csv


class TestMoneyFunctions(unittest.TestCase):

    def setUp(self):
        self.user_data = MagicMock()
        self.user_data.id = 1
        self.user_data.first_name = 'John'
        self.user_data.last_name = 'Doe'
        self.user_data.age = 23
        self.user_data.email = 'john@doe.com'
        self.user_data.money = 500

    @patch('builtins.input', return_value='700')
    @patch("builtins.open", new_callable=mock_open, read_data="id,money\n1,500\n2,1000\n")
    @patch("db.operations.update_log")
    def test_add_money_success(self, mock_update_log, mock_file, mock_input):
        result = add_money(self.user_data)

        self.assertEqual(result, 700)

        mock_update_log.assert_called_once_with(self.user_data)

    @patch("builtins.open", new_callable=mock_open, read_data="id,first_name,last_name,age,email,money,password")
    def test_update_log_success(self, mock_file):
        update_log(self.user_data)

        mock_file.assert_any_call(log_in_path, 'r')

        mock_file.assert_any_call(log_in_path, 'w')

        handle = mock_file()
        handle.write.assert_called()

        expected_calls = [unittest.mock.call().write('id,first_name,last_name,age,email,money,password\r\n')]

        handle.write.assert_has_calls(expected_calls, any_order=True)

    @patch('builtins.input', return_value='-100')
    @patch("builtins.open", new_callable=mock_open, read_data="id,money\n1,500\n2,1000\n")  # Mocking file in update_log
    def test_add_money_negative(self, mock_file, mock_input):
        add_money(self.user_data)

        self.assertEqual(self.user_data.money, 500)

        mock_file().write.assert_not_called()


if __name__ == '__main__':
    unittest.main()
