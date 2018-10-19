import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Leon', 'Lei', 50000)
        self.emp_2 = Employee('John', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Leon.Lei@gmail.com')
        self.assertEqual(self.emp_2.email, 'John.Smith@gmail.com')

        self.emp_1.first = 'Leonidas'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Leonidas.Lei@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Leon Lei')
        self.assertEqual(self.emp_2.fullname, 'John Smith')

        self.emp_1.first = 'Alpha'
        self.emp_2.first = 'Gamma'
        self.emp_1.last = 'Beta'
        self.emp_2.last = 'Delta'

        self.assertEqual(self.emp_1.fullname, 'Alpha Beta')
        self.assertEqual(self.emp_2.fullname, 'Gamma Delta')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Lei/May')
            self.assertEqual(schedule, 'Success')

            # Mock situation where web site is down
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()