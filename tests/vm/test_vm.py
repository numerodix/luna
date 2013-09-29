from luna import objects as obj


def test_ass1(interp_stmt):
    frame = interp_stmt('a = 1')
    assert frame.env == {
        obj.LVar('a'): obj.LNumber(1.0),
    }

def test_binop1(interp_expr):
    frame = interp_expr('1 + 2')
    assert 3 == frame.stack[0].value

def test_call1(interp_stmt, stdout):
    frame = interp_stmt('print(1)')
    assert '1\n' == stdout()

def test_call2(interp_program, stdout):
    frame = interp_program('a = 1\n print(a)')
    assert '1\n' == stdout()
