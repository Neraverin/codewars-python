import unittest

class TestKata(unittest.TestCase):
    def square_digits(self, num):
        return ''.join([str(int(i)*int(i)) for i in str(num)])

    def test1(self):
        self.assertEqual(self.square_digits(9119), 811181)

if __name__ == "__main__":
    unittest.main()