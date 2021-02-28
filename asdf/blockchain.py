from typing import Sequence

from asdf.block import Block, Genesis


class Blockchain:
    def __init__(self) -> None:
        self.chain: Sequence[Block] = [Genesis()]
