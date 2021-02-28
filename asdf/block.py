import json
import os
from time import time
from typing import Sequence


class Block:
    def __init__(
        self, transactions: Sequence[bytes], message: str
    ):
        self.transactions = transactions
        self.message = message
        # timestamp
        # hash
        # prev_hash
        # validator
        # signature


