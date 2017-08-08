# Your goal in this kata is to implement an difference function, which subtracts one list from another.
# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]
import unittest

class TestKata(unittest.TestCase):
    def array_diff(self, a, b):
        print("stub")
        return a

    def test_basic(self):
        self.assertEquals(self.array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEquals(self.array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEquals(self.array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEquals(self.array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEquals(self.array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")


if __name__ == '__main__':
  unittest.main()