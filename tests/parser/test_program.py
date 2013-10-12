from luna.ast import *


def test_seq1(parse_program):
    assert Program(
        Block(
            Stmt(
                Assignment(
                    Lazy(),
                    Lazy(),
                ),
            ),
            Stmt(
                Assignment(
                    Lazy(),
                    Lazy(),
                ),
            ),
        ),
    ) == parse_program(
    '''
        ;
        a = 1;
        ;;;
        b = 1;
        ;;
    '''
    )
