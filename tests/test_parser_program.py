from luna.ast import *


def test_prog1(parse):
    assert Program(
        Stmt(
            Assignment(
                Identifier('a'),
                Lazy(),
            ),
        ),
    ) == parse('a = 1 + 3')

def test_prog2(parse):
    assert Program(
        Stmt(Lazy()),
        Stmt(Lazy()),
    ) == parse('a = 1; print(a)')
