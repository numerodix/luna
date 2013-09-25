from luna.ast import Args
from luna.ast import Assignment
from luna.ast import BinOp
from luna.ast import Boolean
from luna.ast import Call
from luna.ast import Expr
from luna.ast import Identifier
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator
from luna.ast import Stmt
from luna.ast import String
from luna.ast import UnaryOp


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
