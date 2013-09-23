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


def test_float(parse):
    assert Expr(Number('1')) == parse('1')

def test_float2(parse):
    assert Expr(Number('1.')) == parse('1.')

def test_float3(parse):
    assert Expr(Number('.1')) == parse('.1')


def test_expr_eq(parse):
    assert Expr(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
    ) == parse('true == true')

def test_expr_neq(parse):
    assert Expr(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
    ) == parse('true ~= true')


def test_expr_ternary(parse):
    assert Expr(
        Boolean('true'),
        Operator('=='),
        Expr(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse('true == true == true')

def test_expr_paren(parse):
    assert Expr(
        Expr(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
        Operator('=='),
        Boolean('true'),
    ) == parse('( true == true ) == true')

def test_expr_paren2(parse):
    assert Expr(
        Boolean('true'),
        Operator('=='),
        Expr(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse('true == ( true == true )')


def test_expr_quaternary(parse):
    assert Expr(
        Boolean('true'),
        Operator('=='),
        Expr(
            Boolean('true'),
            Operator('=='),
            Expr(
                Boolean('true'),
                Operator('=='),
                Boolean('true'),
            ),
        ),
    ) == parse('true == true == true == true')


def test_expr_nums(parse):
    assert Expr(
        Expr(
            Number('1'),
            Operator('*'),
            Number('2'),
        ),
        Operator('+'),
        Number('3'),
    ) == parse('1 * 2 + 3')

def test_expr_nums2(parse):
    assert Expr(
        Number('1'),
        Operator('+'),
        Expr(
            Number('2'),
            Operator('*'),
            Number('3'),
        ),
    ) == parse('1 + 2 * 3')
