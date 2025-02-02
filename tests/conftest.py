import pytest
from fastapi.testclient import TestClient

from fastz.app import app


@pytest.fixture
def client():
    return TestClient(app)
