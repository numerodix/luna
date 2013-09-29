import pytest

from luna.ast import *


def test_eq():
    assert Boolean('true') == Boolean('true')

def test_neq():
    assert Boolean('true') != Boolean('false')

def test_invalid():
    with pytest.raises(ValueError):
        Boolean(True)


def test_lazy1():
    assert Nil() == Lazy()

def test_lazy2():
    assert Expr(Number('1')) == Expr(Lazy())

def test_lazy3():
    assert Program(Lazy(), Lazy()) != Program(Lazy())

def test_lazy4():
    assert Program(Lazy()) != Program(Lazy(), Lazy())
