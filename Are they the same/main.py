# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether
# the two arrays have the "same" elements, with the same multiplicities. "Same" means, here,
# that the elements in b are the elements in a squared, regardless of the order.

import unittest
import math

class TestKata(unittest.TestCase):
    def comp(self, array1, array2):
        if array1 == None or array2 == None :
            return False
        for i in array2:
            if not array1.count(math.sqrt(i)):
                return False
        return True

    def test1(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertEqual(self.comp(a, b), True)

    def test2(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertEqual(self.comp(a, b), False)

    def test3(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
        self.assertEqual(self.comp(a, b), False)

    def test1(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [121, 14641, 20736, 361, 25920, 361, 20736, 361]
        self.assertEqual(self.comp(a, b), False)

if __name__ == "__main__":
    unittest.main()