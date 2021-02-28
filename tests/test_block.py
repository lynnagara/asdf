from asdf.block import Block
from asdf.wallet import Wallet
from asdf.transaction import Transaction


def test_create_block(key_path: str) -> None:
    sender = Wallet(50, f"{key_path}/wallet1_private.pem")
    sender.generate_key()
    recipient = Wallet(50, f"{key_path}/wallet2_private.pem")
    recipient.generate_key()
    recipient_address = recipient.generate_address()

    transactions = [
        sender.create_signed_transaction(recipient_address, [], 5, 0),
        sender.create_signed_transaction(recipient_address, [], 5, 0),
    ]
    block = Block(transactions=transactions, message="hello world")
