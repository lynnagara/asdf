import os

ROOT_DIR = os.path.dirname(__file__)

GENESIS_PATH = os.getenv("GENESIS_PATH", os.path.join(ROOT_DIR, "genesis.json"))

SERVER_HOST = "localhost"
SERVER_PORT = 8000
MAX_CONNECTIONS = 5