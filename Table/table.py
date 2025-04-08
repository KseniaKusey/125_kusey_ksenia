def rail_fence_cipher_encrypt(message, n):
    # Удаляем пробелы и приводим к нижнему регистру
    message = message.replace(" ", "").lower()
    rail = [['\n' for _ in range(len(message))] for _ in range(n)]

    direction_down = False
    row, col = 0, 0

    for char in message:
        if row == 0:
            direction_down = True
        if row == n - 1:
            direction_down = False

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    encrypted_message = ''.join([''.join(row) for row in rail]).replace('\n', '')
    return encrypted_message


def rail_fence_cipher_decrypt(ciphertext, n):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(n)]
    direction_down = None
    row, col = 0, 0

    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == n - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(n):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*' and index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    decrypted_message = []
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == n - 1:
            direction_down = False

        if rail[row][col] != '\n':
            decrypted_message.append(rail[row][col])
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(decrypted_message)


if __name__ == "__main__":
    original_message = "Hello World"
    shift_value = 3
    encrypted = rail_fence_cipher_encrypt(original_message, 3)
    print(f"Original: {original_message}\nEncrypted: {encrypted}")

    decrypted = rail_fence_cipher_decrypt(encrypted, 3)
    print(f"Decrypted: {decrypted}")
