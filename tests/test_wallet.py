import os
from asdf.wallet import Wallet

BASE_PATH = os.path.join(os.path.dirname(__file__), "tmp")


def teardown_function() -> None:
    os.remove(f"{BASE_PATH}/wallet1_private.pem")
    os.remove(f"{BASE_PATH}/wallet2_private.pem")


def test_sign_and_verify() -> None:
    wallet1 = Wallet(50, f"{BASE_PATH}/wallet1_private.pem")
    wallet1.generate_key()
    wallet1_address = wallet1.generate_address()
    wallet2 = Wallet(50, f"{BASE_PATH}/wallet2_private.pem")
    wallet2.generate_key()
    wallet2_address = wallet2.generate_address()

    txn = wallet1.create_signed_transaction(wallet2_address, [], 5, 0)

    assert wallet2.verify_transaction(txn) is True
