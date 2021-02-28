import os
from asdf.wallet import Wallet


def test_sign_and_verify(key_path: str) -> None:
    wallet1 = Wallet(50, f"{key_path}/wallet1_private.pem")
    wallet1.generate_key()
    wallet1_address = wallet1.generate_address()
    wallet2 = Wallet(50, f"{key_path}/wallet2_private.pem")
    wallet2.generate_key()
    wallet2_address = wallet2.generate_address()

    txn = wallet1.create_signed_transaction(wallet2_address, [], 5, 0)

    assert wallet2.verify_transaction(txn) is True
