import unittest

from RSA.prime import generate_primes
from RSA.realizaton import Rsa


class TestRSA(unittest.TestCase):
    def setUp(self):
        primes = generate_primes(10**6)
        self.rsa = Rsa(primes)

    def test_encryption_decryption(self):
        message = "Test message"
        encrypted = self.rsa.encrypt(message)
        decrypted = self.rsa.decrypt(encrypted)
        self.assertEqual(message, decrypted)

    def test_key_generation(self):
        self.assertTrue(1 < self.rsa.e < self.rsa.phi)
        self.assertTrue(self.rsa.e != self.rsa.p)
        self.assertTrue(self.rsa.e != self.rsa.q)

if __name__ == '__main__':
    unittest.main()
