import importlib
import json
import os
import click


from asdf.errors import WalletExists
from asdf.server import Server
from asdf.validator import Validator
from asdf.wallet import Wallet

@click.group()
def cli() -> None:
    pass


@cli.command()
def generate_mock_data(genesis_path: str = "./genesis.json") -> None:
    wallet = Wallet()

    try:
        wallet.generate_key()
    except WalletExists:
        wallet.load_key()

    address = wallet.generate_address()

    genesis_data = json.dumps({"initial_alloc": {address: "50000"}, "message": ":)"})

    with open(genesis_path, "w") as f:
        f.write(genesis_data)

@cli.command()
def serve() -> None:
   Server().run()

@cli.command()
def run_validator() -> None:
    validator = Validator()
    validator.run()