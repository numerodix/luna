from luna.ast import *


def test_power1(parse_expr):
    assert Expr(
        Power(
            Number('3'),
            Power(
                Number('4'),
                Number('5'),
            ),
        ),
    ) == parse_expr('3 ^ 4 ^ 5')


def test_unary1(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('-'),
            Number('4'),
        ),
    ) == parse_expr('- 4')


def test_term1(parse_expr):
    assert Expr(
        Term(
            Expr(
                Term(
                    Number('2'),
                    Operator('/'),
                    Number('4'),
                ),
            ),
            Operator('*'),
            Number('8'),
        ),
    ) == parse_expr('2 / 4 * 8')


def test_arith1(parse_expr):
    assert Expr(
        Arith(
            Expr(
                Arith(
                    Number('2'),
                    Operator('+'),
                    Number('4'),
                ),
            ),
            Operator('-'),
            Number('8'),
        ),
    ) == parse_expr('2 + 4 - 8')


def test_str1(parse_expr):
    assert Expr(
        Arith(
            Expr(
                Arith(
                    Number('2'),
                    Operator('+'),
                    Number('4'),
                ),
            ),
            Operator('-'),
            Number('8'),
        ),
    ) == parse_expr('2 + 4 - 8')
