class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def _extend_key(self, message):
        key_length = len(self.key)
        message_length = len(message)
        extended_key = []

        for i in range(message_length):
            extended_key.append(self.key[i % key_length])

        return ''.join(extended_key)

    def encrypt(self, message):
        message = message.upper()
        extended_key = self._extend_key(message)
        cipher_text = []

        for m, k in zip(message, extended_key):
            if m in self.alphabet:
                m_index = self.alphabet.index(m)
                k_index = self.alphabet.index(k)
                c_index = (m_index + k_index) % len(self.alphabet)
                cipher_text.append(self.alphabet[c_index])
            else:
                cipher_text.append(m)  # Неизменяем символы, не входящие в алфавит.

        return ''.join(cipher_text)

    def decrypt(self, cipher_text):
        cipher_text = cipher_text.upper()
        extended_key = self._extend_key(cipher_text)
        decrypted_text = []

        for c, k in zip(cipher_text, extended_key):
            if c in self.alphabet:
                c_index = self.alphabet.index(c)
                k_index = self.alphabet.index(k)
                m_index = (c_index - k_index) % len(self.alphabet)
                decrypted_text.append(self.alphabet[m_index])
            else:
                decrypted_text.append(c)  # Неизменяем символы, не входящие в алфавит.

        return ''.join(decrypted_text)


# Пример использования:
if __name__ == "__main__":
    cipher = VigenereCipher("KEY")
    encrypted = cipher.encrypt("HELLO WORLD")
    print("Encrypted:", encrypted)
    decrypted = cipher.decrypt(encrypted)
    print("Decrypted:", decrypted)
