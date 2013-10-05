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


def test_call1(interp_stmt, stdout):
    frame = interp_stmt('print(1)')
    assert '1\n' == stdout()

def test_call2(interp_stmt, stdout):
    frame = interp_stmt('print(1 - 3)')
    assert '-2\n' == stdout()


def test_ass_call1(interp_program, stdout):
    frame = interp_program('a = 1 - 3 + 5\nprint(a)')
    assert '3\n' == stdout()

def test_ass_call2(interp_program, stdout):
    frame = interp_program('a = 1 - 5\nb = a\nprint(b)')
    assert '-4\n' == stdout()

def _test_ass_call3(interp_program):
    frame = interp_program('a = 1 - 5\nb = 7\nprint(a - b)')

def _test_ass_call3(interp_program, stdout):
    frame = interp_program('a = 1 - 5\nb = 7\nprint(a - b)')
    assert '-4\n' == stdout()
