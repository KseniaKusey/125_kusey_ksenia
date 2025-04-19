import random
from sympy import mod_inverse

from RSA.prime import generate_primes


class Rsa:
    def __init__(self, prime):
        self.primes = prime
        self.p = random.choice(prime)
        self.q = random.choice([prime for prime in prime if prime != self.p])
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.find_e()
        self.d = mod_inverse(self.e, self.phi)

    def find_e(self):
        for i in range(2, self.phi):
            if self.gcd(i, self.phi) == 1:
                return i
        return None

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def encrypt(self, plaintext):
        plaintext_bytes = plaintext.encode('utf-8')
        plaintext_int = int.from_bytes(plaintext_bytes, 'big')
        cipher_int = pow(plaintext_int, self.e, self.n)
        return cipher_int

    def decrypt(self, ciphertext):
        decrypted_int = pow(ciphertext, self.d, self.n)
        decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')

        print(f"Decrypted bytes: {decrypted_bytes}")  # Выводим для отладки

        try:
            return decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError as e:
            print(f"Ошибка декодирования: {e}, Байты: {decrypted_bytes}")
            return None


# Пример использования
if __name__ == '__main__':
    primes = generate_primes(10 ** 6)
    rsa = Rsa(primes)

    message = "Hello, RSA!"
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)

    print(f"Original: {message}")
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}")

