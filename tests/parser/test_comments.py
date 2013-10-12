from luna.ast import *


def test_linecomment1(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program(
    '''
        x = 1       -- assign this
        print(x)    -- use x
    '''
    )


def test_multicomment1(parse_program):
    assert Program(
        Block(
            Stmt(Lazy()),
            Stmt(Lazy()),
        ),
    ) == parse_program(
    '''
        x = 1       --[[
            comment
        ]]
        print(x)
    '''
    )
