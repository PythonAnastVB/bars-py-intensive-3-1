import unittest

from tasks.common import specific_func, MyException
from tasks.decorators.task_4.implementation import decorator_maker_function


class MyTestCase(unittest.TestCase):
    def test_on_getting_right_value(self):
        new_factorial = decorator_maker_function(3, 0)(specific_func)
        self.assertEqual(new_factorial(), 1)

    def test_on_getting_incorrect_Value(self):
        new_factorial = decorator_maker_function(4, 0)(specific_func)
        self.assertEqual(new_factorial(), 1)

    def test_on_no_getting_value(self):
        new_factorial = decorator_maker_function(2, 0)(specific_func)
        self.assertRaises(MyException, new_factorial)


if __name__ == '__main__':
    unittest.main()
