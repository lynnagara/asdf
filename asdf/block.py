from typing import Any
import json
import os
from time import time
from typing import Sequence


class Block:
    def __init__(self, transactions: Sequence[bytes], message: str) -> None:
        self.transactions = transactions
        self.message = message
        # timestamp
        # hash
        # prev_hash
        # validator
        # signature

    def __eq__(self, other: Any) -> bool:
        if (
            self.__class__ == other.__class__
            and self.transactions == other.transactions
            and self.message == other.message
        ):
            return True

        return False


class Genesis(Block):
    def __init__(self) -> None:
        path = os.getenv("GENESIS", "genesis.json")
        with open(path) as f:
            data = json.load(f)

        self.message = data["message"]
        self.transactions = data["transactions"]

        assert isinstance(self.message, str)
        assert isinstance(self.transactions, list)

