import json
import zlib
from abc import ABC
from hashlib import sha3_256
from typing import Any, Mapping, Optional
from uuid import uuid4

from ecdsa import SigningKey, VerifyingKey  # type: ignore

SignedTransaction = Mapping[str, Any]


class Transaction:
    def __init__(
        self, from_address: str, to_address: str, amount: int, fee: int, nonce: int = 1
    ) -> None:
        self.version = 1
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.fee = fee
        self.nonce = nonce
        self.signed_transaction: Optional[SignedTransaction] = None

    def sign(self, signing_key: SigningKey) -> SignedTransaction:
        transaction_data = {
            "to_address": self.to_address,
            "amount": self.amount,
            "fee": self.fee,
            "nonce": self.nonce,
        }

        transaction_str = json.dumps(transaction_data).encode()
        transaction_hash = sha3_256(transaction_str).digest()
        verifying_key = signing_key.verifying_key

        signature = signing_key.sign(transaction_hash).hex()

        self.signed_transaction = {
            **transaction_data,
            "version": self.version,
            "signature": signature,
            "public_key": verifying_key.to_string("compressed").hex(),
        }
        return self.signed_transaction

    def serialize(self) -> bytes:
        assert self.signed_transaction is not None
        return zlib.compress(json.dumps(self.signed_transaction).encode("utf-8"))
