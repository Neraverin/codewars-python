# Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below),
# a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
#
# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incrementing: 1234
# The digits are sequential, decrementing: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
#
# Error Checking
# A number is only interesting if it is greater than 99!
# Input will always be an integer greater than 0, and less than 1,000,000,000.
# The awesomePhrases array will always be provided, and will always be an array, but may be empty.
# (Not everyone thinks numbers spell funny words...)
# You should only ever output 0, 1, or 2.

import unittest


class TestKata(unittest.TestCase):
    @staticmethod
    def is_interesting(number, awesome_phrases):
        pass

    def test_example_case(self):
        tests = [
            {'n': 3, 'interesting': [1337, 256], 'expected': 0},
            {'n':3236, 'interesting': [1337, 256], 'expected': 0},
            {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
            {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
            {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
            {'n': 11210, 'interesting': [1337, 256], 'expected': 1},
            {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
            {'n': 1335, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
        ]
        for t in tests:
            self.assertEqual(self.is_interesting(t['n'], t['interesting']), t['expected'])


if __name__ == "__main__":
    unittest.main()
