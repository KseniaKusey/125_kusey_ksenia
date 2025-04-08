def caesar_cipher(message, shift):
    encrypted_message = []

    for char in message:
        if char.isalpha():  # проверяем является ли символ буквой
            shift_base = ord('A') if char.isupper() else ord('a')
            # сдвигаем символ, обрабатывая его по кругу
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)  # не буквы добавляем без изменений

    return ''.join(encrypted_message)


if __name__ == "__main__":
    # Пример использования
    original_message = "Hello, World!"
    shift_value = 3
    encrypted = caesar_cipher(original_message, shift_value)
    print(f"Original: {original_message}\nEncrypted: {encrypted}")
