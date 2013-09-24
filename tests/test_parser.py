from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Identifier
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator
from luna.ast import String


def test_nil(parse):
    assert Nil() == parse('nil', rule='operand')

def test_false(parse):
    assert Boolean('false') == parse('false', rule='operand')

def test_true(parse):
    assert Boolean('true') == parse('true', rule='operand')


def test_float(parse):
    assert Number('1') == parse('1', rule='operand')

def test_float2(parse):
    assert Number('1.') == parse('1.', rule='operand')

def test_float3(parse):
    assert Number('.1') == parse('.1', rule='operand')


def test_string(parse):
    assert String("a'a") == parse("'a\\'a'", rule='string')

def test_string2(parse):
    assert String('a"a') == parse('"a\\"a"', rule='string')


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
