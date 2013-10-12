from luna.ast import *


def test_comment1(parse_program):
    parse_program(
    '''
        x = 1       -- assign this
        print(x)    -- use x
    '''
    )
