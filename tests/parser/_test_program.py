from luna.ast import *


def test_prog1(parse_program):
    assert Program(
        Block(
            Stmt(
                Assignment(
                    Identifier('a'),
                    Lazy(),
                ),
            ),
        ),
    ) == parse_program('a = 1 + 3')


def test_seq1(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program('a = 1;print(a)')

def test_seq2(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program('a = 1; print(a)')

def test_seq3(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program('a = 1 ; print(a)')

def test_seq4(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program('a = 1  ; print(a)')

def test_seq5(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program('a = 1 print(a)')
