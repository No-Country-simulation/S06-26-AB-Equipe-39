"""Fixtures compartilhadas dos testes."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Cliente de teste da API."""
    return TestClient(app)
