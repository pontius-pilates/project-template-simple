"""Example test file to verify pytest is working."""

from src import __version__


def test_version() -> None:
    """Test that version is set correctly."""
    assert __version__ == "0.1.0"


def test_example() -> None:
    """Example test that always passes."""
    assert True
