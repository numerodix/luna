import pytest

from luna.ast import *


def test_eq1():
    assert Boolean('true') == Boolean('true')

def test_eq2():
    assert Nil() == Nil()

def test_eq3():
    assert Args(Boolean('true'), Number('1')) == Args(Boolean('true'), Number('1'))

def test_neq1():
    assert Boolean('true') != Boolean('false')

def test_neq2():
    assert Boolean('true') != Nil()

def test_neq3():
    assert Args(Boolean('true')) != Args(Boolean('true'), Number('1'))

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
