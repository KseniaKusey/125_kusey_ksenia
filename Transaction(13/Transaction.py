from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import json


class Transaction:
    def __init__(self, inputs, outputs, private_key=None):
        self.inputs = inputs  # Список входов
        self.outputs = outputs  # Список выходов
        self.signature = None  # Подпись транзакции

        if private_key is not None:
            self.sign(private_key)

    def sign(self, private_key):
        if isinstance(private_key, str):
            private_key = serialization.load_pem_private_key(
                private_key.encode(),
                password=None,
                backend=default_backend()
            )
        # Подпись транзакции
        transaction_data = json.dumps(self.to_dict(), sort_keys=True).encode()
        self.signature = private_key.sign(
            transaction_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def to_dict(self):
        return {
            'inputs': self.inputs,
            'outputs': self.outputs,
            'signature': self.signature.hex() if self.signature else None
        }

if __name__ == "__main__":
    # Генерация ключей RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    transaction = Transaction(inputs=['input1'], outputs=['output1'], private_key=private_key)

    print("Transaction data:")
    print(transaction.to_dict())
