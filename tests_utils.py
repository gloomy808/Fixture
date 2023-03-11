import pytest

from utils import add, division, f


@pytest.mark.parametrize("a,b,expect", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expect):
    assert add(a, b) == expect


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


@pytest.mark.parametrize("x, expectError", [
    ('1', TypeError),
    ([1], TypeError),
    ((1,), TypeError)
])
def test_f(x, expectError):
    with pytest.raises(expectError):
        f(x)


@pytest.fixture
def connect():
    with open('test.txt', 'a') as f:
        f.write('test')
    return 'test'


def test_division_by_zero(connect):
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


@pytest.fixture
def setup():
    x = [1, 2, 3]
    return x

def test_fixture(setup):
    assert len(setup) == 3
    assert setup == [1, 2, 3]


