import unittest
from cipher import caesar_cipher

class Test(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_cipher("abcd", 1), "bcde")
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_case_sensitivity(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_cipher("hello", 3), "khoor")

    def test_non_alpha_chars(self):
        self.assertEqual(caesar_cipher("Hello, World! 123", 3), "Khoor, Zruog! 123")
        self.assertEqual(caesar_cipher("Test #1", 2), "Vguv #1")

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("abc", -1), "zab")
        self.assertEqual(caesar_cipher("Hello", -2), "Fcjjm")

if __name__ == '__main__':
    unittest.main()