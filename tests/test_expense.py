import unittest
from unittest.mock import Mock
import pendulum
from models.expense import Expense  # Assuming your class is in a file called expense.py


class TestExpense(unittest.TestCase):

    def setUp(self):
        # Common setup for test cases
        self.user_data = Mock()
        self.user_data.id = 1
        self.user_data.money = 500  # Initial amount of money user has

    def test_spend_success(self):
        expense = Expense(spend_amount=100, type_of_expense="mid", category="Food")

        # When the user has enough money
        remaining_money = expense.spend(self.user_data)

        # Check if the user_data's money was decremented correctly
        self.assertEqual(self.user_data.money, 400)
        self.assertEqual(remaining_money, 400)

    def test_spend_fail_insufficient_funds(self):
        expense = Expense(spend_amount=600, type_of_expense="mid", category="Gadgets")

        # When the user does not have enough money
        result = expense.spend(self.user_data)

        # Check if the transaction failed and no money was deducted
        self.assertFalse(result)
        self.assertEqual(self.user_data.money, 500)  # No money should have been deducted

    def test_spend_exact_money(self):
        # Case where the user spends exactly the money they have
        self.user_data.money = 500
        expense = Expense(spend_amount=500, type_of_expense="mid", category="Housing")

        remaining_money = expense.spend(self.user_data)

        self.assertEqual(self.user_data.money, 0)  # All money should be gone
        self.assertEqual(remaining_money, 0)

    def test_to_dict(self):
        expense = Expense(spend_amount=200, type_of_expense="mid", category="Leisure")

        # Ensure the to_dict method returns the correct structure and values
        expense_info = expense.to_dict(self.user_data)

        expected_dict = {
            'user_id': self.user_data.id,
            'amount': 200,
            'type': 'mid',
            'category': 'Leisure',
            'time': expense.time,  # This will be a pendulum datetime object
        }

        self.assertEqual(expense_info['user_id'], expected_dict['user_id'])
        self.assertEqual(expense_info['amount'], expected_dict['amount'])
        self.assertEqual(expense_info['type'], expected_dict['type'])
        self.assertEqual(expense_info['category'], expected_dict['category'])
        self.assertIsInstance(expense_info['time'], pendulum.DateTime)  # Time should be a pendulum datetime

    def test_spend_doesnt_change_user_money_on_fail(self):
        # Make sure money isn't changed when the transaction fails
        self.user_data.money = 300
        expense = Expense(spend_amount=400, type_of_expense="mid", category="Other")

        result = expense.spend(self.user_data)

        # Ensure the user's money hasn't changed
        self.assertEqual(self.user_data.money, 300)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
