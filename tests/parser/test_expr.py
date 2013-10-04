from luna.ast import *


## Highest to lowest precedence: tests for associativity

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
            Term(
                Number('2'),
                Operator('/'),
                Number('4'),
            ),
            Operator('*'),
            Number('8'),
        ),
    ) == parse_expr('2 / 4 * 8')


def test_arith1(parse_expr):
    assert Expr(
        Arith(
            Arith(
                Number('2'),
                Operator('+'),
                Number('4'),
            ),
            Operator('-'),
            Number('8'),
        ),
    ) == parse_expr('2 + 4 - 8')


def test_concat1(parse_expr):
    assert Expr(
        Concat(
            Number('2'),
            Concat(
                Number('8'),
                Number('19'),
            ),
        ),
    ) == parse_expr('2..8..19')


def test_cmp1(parse_expr):
    assert Expr(
        Cmp(
            Cmp(
                Number('2'),
                Operator('<'),
                Number('3'),
            ),
            Operator('>='),
            Number('1'),
        ),
    ) == parse_expr('2 < 3 >= 1')


def test_and1(parse_expr):
    assert Expr(
        And(
            And(
                Number('1'),
                Number('1'),
            ),
            Number('2'),
        ),
    ) == parse_expr('1 and 1 and 2')


def test_or1(parse_expr):
    assert Expr(
        Or(
            Or(
                Number('1'),
                Number('1'),
            ),
            Number('2'),
        ),
    ) == parse_expr('1 or 1 or 2')


## Precedence

def test_mixedops1(parse_expr):
    assert Expr(
        Arith(
            Term(
                Number('5'),
                Operator('*'),
                Power(
                    Number('4'),
                    Number('2'),
                ),
            ),
            Operator('+'),
            Number('9'),
        ),
    ) == parse_expr('5 * 4 ^ 2 + 9')


def test_mixedops2(parse_expr):
    assert Expr(
        Term(
            Expr(
                Arith(
                    Number('1'),
                    Operator('+'),
                    Number('3'),
                ),
            ),
            Operator('*'),
            Number('4'),
        ),
    ) == parse_expr('(1 + 3) * 4')


def test_mixedops3(parse_expr):
    assert Expr(
        Or(
            And(
                UnaryOp(
                    Operator('not'),
                    Number('3'),
                ),
                Number('3'),
            ),
            Cmp(
                Number('4'),
                Operator('>'),
                Number('4'),
            ),
        ),
    ) == parse_expr('not 3 and 3 or 4 > 4')


## Funccalls

def test_funcall1(parse_expr):
    assert Expr(
        Call(
            Identifier('print'),
            Args(
                Identifier('x'),
            ),
        ),
    ) == parse_expr('print(x)')

def test_funcall2(parse_expr):
    assert Expr(
        Call(
            Identifier('print'),
            Args(
                parse_expr('x and y'),
                parse_expr('z'),
            ),
        ),
    ) == parse_expr('print(x and y, z)')
