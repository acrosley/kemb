"""Shared pytest fixtures: keep tests hermetic by stubbing the API key."""
from __future__ import annotations

import os

import pytest


@pytest.fixture(autouse=True)
def _stub_api_key(monkeypatch):
    """Ensure every test runs with a fake LLAMA_CLOUD_API_KEY in the env.

    A handful of code paths call `require_api_key()` even when the network
    call is mocked out; without this fixture they'd `sys.exit(2)`.
    """
    monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "test-key-not-real")
    yield
