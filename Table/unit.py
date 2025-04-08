import unittest
from table import rail_fence_cipher_encrypt, rail_fence_cipher_decrypt

class TestRailFenceCipher(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(rail_fence_cipher_encrypt("Hello World", 3), "Hoo!lrdol elW")
        self.assertEqual(rail_fence_cipher_encrypt("This is a test", 2), "Ti hst e s a t")
        self.assertEqual(rail_fence_cipher_encrypt("Python", 3), "Pyhnot")

    def test_decryption(self):
        self.assertEqual(rail_fence_cipher_decrypt("Hoo!lrdol elW", 3), "hello world")
        self.assertEqual(rail_fence_cipher_decrypt("Ti hst e s a t", 2), "this is a test")
        self.assertEqual(rail_fence_cipher_decrypt("Pyhnot", 3), "python")

if __name__ == '__main__':
    unittest.main()