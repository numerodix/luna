from luna.ast import *


def test_ass1(parse_stmt):
    assert Stmt(
        Assignment(
            Identifier('a'),
            Expr(
                Number('1'),
            ),
        ),
    ) == parse_stmt('a = 1')


def test_call1(parse_stmt):
    assert Stmt(
        Call(
            Identifier('f'),
            Args(
                Expr(
                    Number('1'),
                ),
                Expr(
                    Number('2'),
                ),
                Expr(
                    Number('3'),
                ),
            ),
        ),
    ) == parse_stmt('f(1, 2, 3)')
