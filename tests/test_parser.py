from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Infix
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator


def test_nil(parse):
    assert Expr(Nil()) == parse('nil')

def test_false(parse):
    assert Expr(Boolean('false')) == parse('false')

def test_true(parse):
    assert Expr(Boolean('true')) == parse('true')


def test_expr_eq(parse):
    assert Expr(
        Infix(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        )
    ) == parse('true == true')

def test_expr_neq(parse):
    assert Expr(
        Infix(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
        )
    ) == parse('true ~= true')

def test_expr_quaternary(parse):
    assert Expr(
        Infix(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        )
    ) == parse('true == true == true == true')


def test_expr_plus(parse):
    assert Expr(
        Infix(
            Number('1'),
            Operator('+'),
            Number('2'),
        )
    ) == parse('1 + 2')
