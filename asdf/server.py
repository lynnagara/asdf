import logging
import multiprocessing
import signal
import socket
import time
from typing import Any

from asdf import settings
from asdf.wallet import Wallet

logger = multiprocessing.log_to_stderr(logging.DEBUG)


class Server:
    def worker(self, socket: Any) -> None:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        while True:
            client, address = socket.accept()
            logger.debug("{u} connected".format(u=address))
            client.send("OK".encode())
            client.close()

    def run(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((settings.SERVER_HOST, settings.SERVER_PORT))
        self.socket.listen()

        processes = [
            multiprocessing.Process(target=self.worker, args=(self.socket,))
            for i in range(settings.MAX_CONNECTIONS)
        ]

        for process in processes:
            process.daemon = True
            process.start()

        while True:
            try:
                time.sleep(10)
            except:
                break
