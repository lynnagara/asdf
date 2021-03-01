from typing import Any
import json
import os
from time import time
from typing import Sequence

from asdf.transaction import GenesisTransaction


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

        message = data["message"]
        initial_alloc = data["initial_alloc"]
        assert isinstance(message, str)

        transactions = []

        for alloc in initial_alloc.items():
            address = alloc[0]
            amount = int(alloc[1])
            transactions.append(GenesisTransaction(address, amount))

        self.message = message
        self.transactions = transactions
