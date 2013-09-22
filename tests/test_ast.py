import pytest

from luna.ast import Boolean


def test_eq():
    assert Boolean('true') == Boolean('true')

def test_neq():
    assert Boolean('true') != Boolean('false')

def test_invalid():
    with pytest.raises(ValueError):
        Boolean(True)
