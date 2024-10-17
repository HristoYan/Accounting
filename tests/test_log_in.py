import unittest
from models.log_in import UserLog
from unittest.mock import patch


class TestUserLog(unittest.TestCase):
    @patch('models.log_in.UserLog.get_next_id', return_value=1)
    def test_register_initialization(self, mock_get_next_id):
        # Following some best practices when writing unit test is important.
        # Read more here:
        # https://docs.pytest.org/en/latest/explanation/anatomy.html

        # Arrange
        first_name = 'John'
        last_name = 'Doe'
        age = 23
        email = 'john@doe.com'
        money = 1000
        password = '1234'

        # Act
        reg = UserLog(first_name, last_name, age, email, money, password)

        # Assert
        self.assertEqual(reg.id, 1)
        self.assertEqual(reg.first_name, 'John')
        self.assertEqual(reg.last_name, 'Doe')
        self.assertEqual(reg.age, 23)
        self.assertEqual(reg.email, 'john@doe.com')
        self.assertEqual(reg.money, 1000)
        self.assertEqual(reg._password, '1234')
        mock_get_next_id.assert_called_once()

    # This test is unnecessary now but could be useful
    # if we had complex logic in the get_next_id method
    @patch('models.log_in.UserLog.get_next_id', return_value=1)
    def test_reg_id_assignment(self, mock_get_next_id):
        # Arrange/Act
        reg = UserLog('John', 'Doe', 23, 'john@doe.com', 1000, '1234')

        # Assert
        self.assertEqual(reg.id, 1)
        mock_get_next_id.assert_called_once()

    @patch('models.log_in.UserLog.get_next_id', return_value=1)
    def test_to_dict_method(self, mock_get_next_id):
        # Arrange
        reg = UserLog('John', 'Doe', 23, 'john@doe.com', 1000, '1234')

        # Act
        reg_dict = reg.to_dict()

        # Assert
        assert_dict = {
            'id': reg.id,
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 23,
            'email': 'john@doe.com',
            'money': 1000,
            'password': '1234'
        }
        self.assertEqual(reg_dict, assert_dict)


if __name__ == '__main__':
    unittest.main()
