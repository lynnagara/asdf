from asdf.block import Genesis
from asdf.blockchain import Blockchain


def test_init_blockchain() -> None:
    bc = Blockchain()
    assert bc.chain == [Genesis()]
