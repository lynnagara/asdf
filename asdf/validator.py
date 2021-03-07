import json
import socket
import time
from typing import List, Tuple

from asdf import settings
from asdf.wallet import Wallet

bufsize = 1024

class Validator:
    def __init__(self, wallet_key_path: str = "./private.pem") -> None:
        self.wallet = Wallet(key_path=wallet_key_path)
        self.peers: List[Tuple[str, int]] = []

    def get_peers(self) -> List[Tuple[str, int]]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), settings.SERVER_PORT))
        message = s.recv(bufsize)
        return json.loads(message.decode("utf-8"))

    def run(self) -> None:
        print("getting peers")
        self.peers = self.get_peers()
        print(self.peers)

        while True:
            try:
                time.sleep(10)
            except:
                break


