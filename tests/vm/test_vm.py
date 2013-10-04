from luna import objects as obj


def test_ass1(interp_stmt):
    frame = interp_stmt('a = 1')
    assert frame.env == {
        obj.LVar('a'): obj.LNumber(1.0),
    }

def test_ass2(interp_stmt):
    frame = interp_stmt('a = 1 - 2')
    assert frame.env == {
        obj.LVar('a'): obj.LNumber(-1.0),
    }


def test_arith1(interp_expr):
    frame = interp_expr('1 + 2 + 4')
    assert 7 == frame.stack[0].value

def test_arith2(interp_expr):
    frame = interp_expr('1 - 2 - 5')
    assert -6 == frame.stack[0].value

