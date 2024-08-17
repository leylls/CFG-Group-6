import unittest
from front_end.ft_end_input_utils import *


class TestingInputValidation(unittest.TestCase):

    def test_clean(self):
        inputs_y = ["yes", "y", "YES", "--.;YES", "!.[yes"]
        inputs_n = ["no", "n", "NO", "nope", "nope!!-", ".,NO"]
        for input in inputs_y:
            self.assertEqual("y", clean(input))
        for input in inputs_n:
            self.assertEqual("n", clean(input))
    def test_choice_validation(self):
        result = choice_validation("y", str)
        self.assertEqual(True, result)



if __name__ == '__main__':
    unittest.main()
