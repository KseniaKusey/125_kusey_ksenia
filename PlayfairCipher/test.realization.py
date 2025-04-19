import unittest

from PlayfairCipher.realization import PlayfairCipher


class TestPlayfairCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = PlayfairCipher("KEYWORD")

    def test_encryption(self):
        self.assertEqual(self.cipher.encrypt("HELLO"), "DGFHO")
        self.assertEqual(self.cipher.encrypt("WORLD"), "NRVXA")
        self.assertEqual(self.cipher.encrypt("ATTACK AT DAWN"), "CUTEWHTREU")

    def test_decryption(self):
        self.assertEqual(self.cipher.decrypt("DGFHO"), "HELLO")
        self.assertEqual(self.cipher.decrypt("NRVXA"), "WORLD")
        self.assertEqual(self.cipher.decrypt("CUTEWHTREU"), "ATTACKATDAWN")

    def test_double_letters(self):
        self.assertEqual(self.cipher.encrypt("BALLOON"), "BAXLOON")  # 'L' должен трансформироваться в 'X'
        self.assertEqual(self.cipher.decrypt("BAXLOON"), "BALLOON")

    def test_odd_length(self):
        self.assertEqual(self.cipher.encrypt("HELLO!"), "DGFHOX")  # 'X' добавляется
        self.assertEqual(self.cipher.decrypt("DGFHOX"), "HELLOX")

if __name__ == "__main__":
    unittest.main()
