from luna.ast import *


def _test_linecomment1(parse_program):
    parse_program(
    '''
        x = 1       -- assign this
        print(x)    -- use x
    '''
    )


def test_multicomment1(parse_program):
    parse_program(
    '''
        x = --[[ comment ]] 1       --[[
            comment
        ]]
        print(x)
    '''
    )
