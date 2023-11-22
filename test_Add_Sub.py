import pytest


def test_addition():
    assert 1 + 1 == 2


def test_subtraction():
    assert 5 - 3 == 2


if __name__ == "__main__":
    pytest.main(['-v'])
