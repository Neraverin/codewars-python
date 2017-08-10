import unittest


class KataTest(unittest.TestCase):
    @staticmethod
    def decrypt(encrypted_text, n):
        for i in range(n):
            first = encrypted_text[:int(len(encrypted_text)/2)]
            second = encrypted_text[int(len(encrypted_text)/2):]
            if len(first) < len(second):
                first += ' '
            encrypted_text = ''.join(i for j in zip(second, first) for i in j).rstrip()

        return encrypted_text


    @staticmethod
    def encrypt(text, n):
        for i in range(n):
            text = text[1::2] + text[0::2]

        return text

    def test_empty_case(self):
        self.assertEqual(self.encrypt("", 0), "")
        self.assertEqual(self.decrypt("", 0), "")
        self.assertEqual(self.encrypt(None, 0), None)
        self.assertEqual(self.decrypt(None, 0), None)

    def test_encrypt_case(self):
        self.assertEqual(self.encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(self.encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(self.encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(self.encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(self.encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(self.encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(self.encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

    def test_decrypt_case(self):
        self.assertEqual(self.decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(self.decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(self.decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(self.decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(self.decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(self.decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(self.decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")


if __name__ == "__main__":
    unittest.main()
