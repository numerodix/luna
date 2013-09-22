from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Infix
from luna.ast import Nil
from luna.ast import Operator


def test_nil(parser):
    assert Expr(Nil()) == parser.parse('nil')

def test_false(parser):
    assert Expr(Boolean('false')) == parser.parse('false')

def test_true(parser):
    assert Expr(Boolean('true')) == parser.parse('true')


def test_expr_eq(parser):
    assert Expr(
        Infix(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        )
    ) == parser.parse('true == true')

def test_expr_neq(parser):
    assert Expr(
        Infix(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
        )
    ) == parser.parse('true ~= true')
