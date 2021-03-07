import json
import logging
import multiprocessing
import signal
import socket
import time
from typing import Any, List

from asdf import settings

logger = multiprocessing.log_to_stderr(logging.DEBUG)


class Server:
    def worker(self, socket: Any) -> None:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        while True:
            client, address = socket.accept()
            self.connections.append(address)
            logger.debug("{u} connected".format(u=address))
            connections_copy = [conn for conn in self.connections]
            data = json.dumps(connections_copy).encode()
            client.send(data)
            client.close()

    def run(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((settings.SERVER_HOST, settings.SERVER_PORT))
        self.socket.listen()

        with multiprocessing.Manager() as manager:
            self.connections = manager.list([])

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
