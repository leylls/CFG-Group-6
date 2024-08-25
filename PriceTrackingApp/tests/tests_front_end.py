import unittest
from front_end.ft_end_input_utils import *


class TestingInputValidation(unittest.TestCase):

    def test_clean(self):
        inputs_y = ["yes", "y", "YES", "--.;YES", "!.[yes", "yeah!!!"]
        inputs_n = ["no", "n", "NO", "nope", "nope!!-", ".,NO"]
        input_nums = ["2", "3.5", "194.50"]
        for input in inputs_y:
            self.assertEqual("y", clean(input))
        for input in inputs_n:
            self.assertEqual("n", clean(input))
        for input in input_nums:
            self.assertEqual(input, clean(input))

    def test_choice_validation_str(self):
        tests_cases = ["y", "n"]
        for input in tests_cases:
            self.assertEqual(True, choice_validation(input, str))
    def test_choice_validation_int(self):
        # When exit_opt is True then 0 is a valid answer;
        # so in a case where max_valid_opt is 5, these are the valid inputs: ["0", "1", "2", "3", "4"]
        valid_test_cases = [{'input': "4", 'max_valid_opt': 5, 'exit_opt': True},
                            {'input': "2", 'max_valid_opt': 3, 'exit_opt': True},
                            {'input': "1", 'max_valid_opt': 2, 'exit_opt': True},
                            {'input': "0", 'max_valid_opt': 2, 'exit_opt': True}]
        invalid_test_cases = [
                              {'input': "5", 'max_valid_opt': 5, 'exit_opt': True},
                              {'input': "6", 'max_valid_opt': 5, 'exit_opt': False},
                              {'input': "hey", 'max_valid_opt': 5, 'exit_opt': True},
                              {'input': 3, 'max_valid_opt': 2, 'exit_opt': True},
                              {'input': "0", 'max_valid_opt': 3,'exit_opt': False}]
        for case in valid_test_cases:
            self.assertEqual(True,
                             choice_validation(case['input'], int,
                             num_choices=case['max_valid_opt'], exit_option=case['exit_opt']))
        for case in invalid_test_cases:
            self.assertEqual(False,
                             choice_validation(case['input'], int,
                            num_choices=case['max_valid_opt'], exit_option=case['exit_opt']),
                             "'Please only type one of the given options!' message should also print out")


class TestingEmailValidation(unittest.TestCase):
    def test_is_valid_email(self):
        test_cases = ["eva@cfgdegree", "evacfgdegree.com", "eva@cfgdegreecom", "thisisanemail"]
        for test in test_cases:
            self.assertEqual(False, is_valid_email(test), "'The given email is not the correct format. Try again!' message should also print out")
        self.assertEqual( True, is_valid_email("eva@fakeemail.com"))


if __name__ == '__main__':
    unittest.main()
