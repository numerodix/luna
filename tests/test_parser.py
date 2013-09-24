from luna.ast import BinOp
from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Identifier
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator
from luna.ast import String
from luna.ast import UnaryOp


def test_nil(parse_operand):
    assert Nil() == parse_operand('nil')

def test_false(parse_operand):
    assert Boolean('false') == parse_operand('false')

def test_true(parse_operand):
    assert Boolean('true') == parse_operand('true')


def test_float1(parse_operand):
    assert Number('1') == parse_operand('1')

def test_float2(parse_operand):
    assert Number('1.') == parse_operand('1.')

def test_float3(parse_operand):
    assert Number('.1') == parse_operand('.1')


def test_string1(parse_operand):
    assert String("a'a") == parse_operand("'a\\'a'")

def test_string2(parse_operand):
    assert String('a"a') == parse_operand('"a\\"a"')


def test_expr_unary1(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('not'),
            Boolean('true'),
        ),
    ) == parse_expr('not true')

def test_expr_unary2(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('not'),
            Expr(
                UnaryOp(
                    Operator('not'),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('not not true')


def test_expr_eq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('true == true')

def test_expr_neq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
        ),
    ) == parse_expr('true ~= true')


def test_expr_paren1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('( true == true ) == true')

def test_expr_paren2(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('true == ( true == true )')


def test_expr_ternary(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('true == true == true')

def test_expr_quaternary(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Expr(
                        BinOp(
                            Boolean('true'),
                            Operator('=='),
                            Boolean('true'),
                        ),
                    ),
                ),
            ),
        ),
    ) == parse_expr('true == true == true == true')


def test_expr_nums1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('1'),
                    Operator('*'),
                    Number('2'),
                ),
            ),
            Operator('+'),
            Number('3'),
        ),
    ) == parse_expr('1 * 2 + 3')

def test_expr_nums2(parse_expr):
    assert Expr(
        BinOp(
            Number('1'),
            Operator('+'),
            Expr(
                BinOp(
                    Number('2'),
                    Operator('*'),
                    Number('3'),
                ),
            ),
        ),
    ) == parse_expr('1 + 2 * 3')

def test_expr_nums3(parse_expr):
    Expr(
        BinOp(
            Expr(
                UnaryOp(
                    Operator('-'),
                    Number('1'),
                ),
            ),
            Operator('+'),
            Number('1'),
        ),
    ) == parse_expr('-1 + 1')
