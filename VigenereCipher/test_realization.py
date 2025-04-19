import unittest

from VigenereCipher.realization import VigenereCipher


class TestVigenereCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = VigenereCipher("KEY")

    def test_encryption(self):
        self.assertEqual(self.cipher.encrypt("HELLO"), "RIJVS")
        self.assertEqual(self.cipher.encrypt("WORLD"), "HXFST")
        self.assertEqual(self.cipher.encrypt("TEST MESSAGE"), "WKTW EYGCCB")

    def test_decryption(self):
        self.assertEqual(self.cipher.decrypt("RIJVS"), "HELLO")
        self.assertEqual(self.cipher.decrypt("HXFST"), "WORLD")
        self.assertEqual(self.cipher.decrypt("WKTW EYGCCB"), "TEST MESSAGE")

    def test_non_alpha(self):
        self.assertEqual(self.cipher.encrypt("HELLO, WORLD!"), "RIJVS, HXFST!")
        self.assertEqual(self.cipher.decrypt("RIJVS, HXFST!"), "HELLO, WORLD!")


if __name__ == "__main__":
    unittest.main()

