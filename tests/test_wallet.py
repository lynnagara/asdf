import os
from asdf.wallet import Wallet


def test_sign_and_verify(tmp_path: str) -> None:
    wallet1 = Wallet(50, f"{tmp_path}/wallet1_private.pem")
    wallet1.generate_key()
    wallet1_address = wallet1.generate_address()
    wallet2 = Wallet(50, f"{tmp_path}/wallet2_private.pem")
    wallet2.generate_key()
    wallet2_address = wallet2.generate_address()

    txn = wallet1.create_signed_transaction(wallet2_address, [], 5, 0)

    assert wallet2.verify_transaction(txn) is True


def test_load_pem(tmp_path: str) -> None:
    wallet1_key = Wallet(50, f"{tmp_path}/wallet1_private.pem").generate_key()
    wallet2_key = Wallet(50, f"{tmp_path}/wallet2_private.pem").generate_key()

    loaded_key = Wallet(50, f"{tmp_path}/wallet1_private.pem").load_key()

    assert loaded_key == wallet1_key
    assert loaded_key != wallet2_key
