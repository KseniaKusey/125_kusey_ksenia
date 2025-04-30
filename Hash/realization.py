import hashlib


def hash_function(input_bytes):
    """Хэш-функция, которая принимает массив байт и возвращает хэш фиксированной длины 32 байта"""
    if not isinstance(input_bytes, (bytes, bytearray)):
        raise TypeError("Входные данные должны быть массивом байт (bytes или bytearray).")

    # Используем SHA-256 для получения 32-байтового хэша
    hash_object = hashlib.sha256()
    hash_object.update(input_bytes)
    return hash_object.digest()



if __name__ == '__main__':
    input_data = b"Hello, World!"
    hash_value = hash_function(input_data)
    print(f"Входные данные: {input_data}")
    print(f"Хэш: {hash_value.hex()}")
