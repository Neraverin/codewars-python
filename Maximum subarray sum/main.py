# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array
# or list of integers:
#
# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray

import unittest


class TestKata(unittest.TestCase):
    @staticmethod
    def maxSequence(arr):
        max_sum = 0
        for i in range(1, len(arr) + 1):
            for j in range(0, len(arr) - i + 1):
                if sum(arr[j:j + i]) > max_sum:
                    max_sum = sum(arr[j:j + i])

        return max_sum

    def test_zero_case(self):
        self.assertEqual(self.maxSequence([]), 0)

    def test_example_case(self):
        self.assertEqual(self.maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_negative_case(self):
        self.assertEqual(self.maxSequence([-1, -2, -5, -3, -2, -7]), 0)


if __name__ == "__main__":
    unittest.main()
