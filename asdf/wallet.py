import json
import zlib
from hashlib import sha3_256
from os import path
from typing import Any, Mapping, Optional, Tuple

from asdf.transaction import Transaction
from ecdsa import SECP256k1, SigningKey, VerifyingKey  # type: ignore


class Wallet:
    def __init__(self, balance: int = 0, key_path: str = "./private.pem") -> None:
        self.balance = balance
        self.key_path = key_path
        self.key: Optional[SigningKey] = None

    def generate_key(self) -> SigningKey:
        if path.exists(self.key_path):
            raise Exception(f"{self.key_path} already exists")

        self.key = SigningKey.generate(curve=SECP256k1)
        with open(self.key_path, "wb") as f:
            f.write(self.key.to_pem())

        return self.key

    def load_key(self) -> SigningKey:
        with open(self.key_path, "rb") as f:
            pem = f.read()

        self.key = SigningKey.from_pem(pem)
        return self.key

    def generate_address(self) -> str:
        # Note: generated address doesn't change
        assert self.key is not None
        hex_key = self.key.verifying_key.to_string("compressed").hex().encode()

        return sha3_256(hex_key).hexdigest()

    def create_signed_transaction(
        self, recipient: str, blockchain: Any, amount: int, fee: int
    ) -> bytes:
        assert self.key is not None

        assert amount + fee <= self.balance

        transaction = Transaction(
            from_address=self.generate_address(),
            to_address=recipient,
            amount=amount,
            fee=fee,
        )
        transaction.sign(self.key)
        return transaction.serialize()

    def verify_transaction(self, raw_transaction: bytes) -> bool:
        deserialized = json.loads(zlib.decompress(raw_transaction).decode("utf-8"))
        public_key = bytes(bytearray.fromhex(deserialized["public_key"]))
        signature = bytes.fromhex(deserialized["signature"])
        verifying_key = VerifyingKey.from_string(public_key, curve=SECP256k1)

        expected = sha3_256(
            json.dumps(
                {
                    "to_address": deserialized["to_address"],
                    "amount": deserialized["amount"],
                    "fee": deserialized["fee"],
                    "nonce": deserialized["nonce"],
                }
            ).encode()
        ).digest()

        is_valid: bool = verifying_key.verify(signature, expected)

        return is_valid
