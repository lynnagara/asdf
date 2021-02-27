import os
import pytest
from typing import Any, Iterator


@pytest.fixture(autouse=True)
def create_tmp() -> Iterator[Any]:
    path = os.path.join(os.path.dirname(__file__), "tmp")

    if not os.path.exists(path):
        os.makedirs(path)

    yield
