import pytest


@pytest.fixture
def a():
    return 3
@pytest.fixture
def b():
    return 9

def test_func(a,b):
    assert a**2 == b

test_func(4,16)