from luna.ast import *


def test_prog1(parse):
    assert Program(
        Block(
            Stmt(
                Assignment(
                    Identifier('a'),
                    Lazy(),
                ),
            ),
        ),
    ) == parse('a = 1 + 3')


def test_seq1(parse):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse('a = 1;print(a)')

def test_seq2(parse):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse('a = 1; print(a)')

def test_seq3(parse):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse('a = 1 ; print(a)')

def test_seq4(parse):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse('a = 1  ; print(a)')

def test_seq5(parse):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse('a = 1 print(a)')
