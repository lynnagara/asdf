import os
import pytest
from typing import Any, Iterator


@pytest.fixture
def key_path() -> str:
    return os.path.join(os.path.dirname(__file__), "tmp")


@pytest.fixture(autouse=True)
def create_tmp(key_path: str) -> Iterator[Any]:
    path = os.path.join(os.path.dirname(__file__), "tmp")

    if not os.path.exists(path):
        os.makedirs(path)

    yield

    for entry in os.scandir(key_path):
        if entry.is_file():
            os.remove(f"{key_path}/{entry.name}")
