class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper().replace("J", "I")
        self.table = self._create_table()

    def _create_table(self):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_table = []
        used_characters = set()

        for char in self.key:
            if char in alphabet and char not in used_characters:
                used_characters.add(char)
                key_table.append(char)

        for char in alphabet:
            if char not in used_characters:
                used_characters.add(char)
                key_table.append(char)

        return [key_table[i:i + 5] for i in range(0, len(key_table), 5)]

    def _get_pair(self, a, b):
        if a == b:
            b = 'X'  # Заменить дублирующийся символ 'X'
        return a, b

    def _find_position(self, char):
        for i, row in enumerate(self.table):
            if char in row:
                return i, row.index(char)
        return None  # не должно произойти для правильного ключа

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        pairs = []

        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            b = plaintext[i + 1] if (i + 1) < len(plaintext) else 'X'  # добавляем 'X' если один символ
            a, b = self._get_pair(a, b)
            pairs.append((a, b))
            i += 2

        encrypted_text = []
        for a, b in pairs:
            r1, c1 = self._find_position(a)
            r2, c2 = self._find_position(b)

            if r1 == r2:  # В одной строке
                encrypted_text.append(self.table[r1][(c1 + 1) % 5])
                encrypted_text.append(self.table[r2][(c2 + 1) % 5])
            elif c1 == c2:  # В одном столбце
                encrypted_text.append(self.table[(r1 + 1) % 5][c1])
                encrypted_text.append(self.table[(r2 + 1) % 5][c2])
            else:  # В разных строках и столбцах
                encrypted_text.append(self.table[r1][c2])
                encrypted_text.append(self.table[r2][c1])

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace("J", "I")
        pairs = []

        i = 0
        while i < len(ciphertext):
            a = ciphertext[i]
            b = ciphertext[i + 1] if (i + 1) < len(ciphertext) else 'X'
            pairs.append((a, b))
            i += 2

        decrypted_text = []
        for a, b in pairs:
            r1, c1 = self._find_position(a)
            r2, c2 = self._find_position(b)

            if r1 == r2:
                decrypted_text.append(self.table[r1][(c1 - 1) % 5])
                decrypted_text.append(self.table[r2][(c2 - 1) % 5])
            elif c1 == c2:
                decrypted_text.append(self.table[(r1 - 1) % 5][c1])
                decrypted_text.append(self.table[(r2 - 1) % 5][c2])
            else:
                decrypted_text.append(self.table[r1][c1])
                decrypted_text.append(self.table[r2][c2])

        return ''.join(decrypted_text)


# Пример использования
if __name__ == "__main__":
    cipher = PlayfairCipher("KEYWORD")
    encrypted = cipher.encrypt("HELLO WORLD")
    print("Encrypted:", encrypted)
    decrypted = cipher.decrypt(encrypted)
    print("Decrypted:", decrypted)
