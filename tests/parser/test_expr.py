from luna.ast import *


## Lowest to highest precedence: tests for associativity

def test_power1(parse_expr):
    assert Expr(
        Power(
            Number('3'),
            Expr(
                Power(
                    Number('4'),
                    Number('5'),
                ),
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


def test_concat1(parse_expr):
    assert Expr(
        Concat(
            Number('2'),
            Expr(
                Concat(
                    Number('8'),
                    Number('19'),
                ),
            ),
        ),
    ) == parse_expr('2..8..19')


def test_cmp1(parse_expr):
    assert Expr(
        Cmp(
            Expr(
                Cmp(
                    Number('2'),
                    Operator('<'),
                    Number('3'),
                ),
            ),
            Operator('>='),
            Number('1'),
        ),
    ) == parse_expr('2 < 3 >= 1')


def test_and1(parse_expr):
    assert Expr(
        And(
            Expr(
                And(
                    Number('1'),
                    Number('1'),
                ),
            ),
            Number('2'),
        ),
    ) == parse_expr('1 and 1 and 2')


def test_or1(parse_expr):
    assert Expr(
        Or(
            Expr(
                Or(
                    Number('1'),
                    Number('1'),
                ),
            ),
            Number('2'),
        ),
    ) == parse_expr('1 or 1 or 2')


## Precedence

def test_power_unary1(parse_expr):
    assert Expr(
        Arith(
            Expr(
                Term(
                    Number('5'),
                    Operator('*'),
                    Expr(
                        Power(
                            Number('4'),
                            Number('2'),
                        ),
                    ),
                ),
            ),
            Operator('+'),
            Number('9'),
        ),
    ) == parse_expr('5 * 4 ^ 2 + 9')
