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


def test_do1(parse_stmt):
    assert Stmt(
        Do(
            Block(
                Stmt(
                    Call(
                        Lazy(),
                        Lazy(),
                    ),
                ),
            ),
        ),
    ) == parse_stmt('do print(1) end')
