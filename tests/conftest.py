import json
import os
from typing import Any, Iterator
from unittest import mock

import pytest

os.environ["GENESIS_PATH"] = os.path.join(
    os.path.dirname(__file__), "tmp", "genesis.json"
)


@pytest.fixture
def tmp_path() -> str:
    return os.path.join(os.path.dirname(__file__), "tmp")


@pytest.fixture(autouse=True)
def create_genesis_json(tmp_path: str) -> None:
    genesis_data = json.dumps({"initial_alloc": {}, "message": ":)"})

    with open(os.path.join(tmp_path, "genesis.json"), "w") as f:
        f.write(genesis_data)


@pytest.fixture(autouse=True)
def create_tmp(tmp_path: str) -> Iterator[Any]:
    path = os.path.join(os.path.dirname(__file__), "tmp")

    if not os.path.exists(path):
        os.makedirs(path)

    yield

    for entry in os.scandir(tmp_path):
        if entry.is_file():
            os.remove(f"{tmp_path}/{entry.name}")
