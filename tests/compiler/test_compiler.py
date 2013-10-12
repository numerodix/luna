from luna import objects as obj
from luna.vm import opcodes as ops


def test_ass1(compile_stmt):
    frame = compile_stmt('a = 1')

    assert frame.code == [
        ops.LoadConst(0),
        ops.StoreName(0),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
    ]
    assert frame.vars == [
        obj.LVar('a'),
    ]

def test_ass2(compile_stmt):
    frame = compile_stmt('a = b')

    assert frame.code == [
        ops.LoadName(0),
        ops.StoreName(1),
    ]
    assert frame.vars == [
        obj.LVar('b'),
        obj.LVar('a'),
    ]

def test_ass3(compile_stmt):
    frame = compile_stmt('a = 1 - 2')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.BinarySubtract(),
        ops.StoreName(0),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
    ]
    assert frame.vars == [
        obj.LVar('a'),
    ]


def test_arith1(compile_expr):
    frame = compile_expr('1 - 2')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.BinarySubtract(),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
    ]

def test_arith2(compile_expr):
    frame = compile_expr('a - b')

    assert frame.code == [
        ops.LoadName(0),
        ops.LoadName(1),
        ops.BinarySubtract(),
    ]
    assert frame.vars == [
        obj.LVar('a'),
        obj.LVar('b'),
    ]

def test_arith3(compile_expr):
    frame = compile_expr('1 - 2 - 3')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.BinarySubtract(),
        ops.LoadConst(2),
        ops.BinarySubtract(),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
        obj.LNumber(3.0),
    ]


def test_call1(compile_expr):
    frame = compile_expr('print(1)')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadName(0),
        ops.Call()
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
    ]
    assert frame.vars == [
        obj.LVar('print')
    ]

def test_call2(compile_expr):
    frame = compile_expr('print(b)')

    assert frame.code == [
        ops.LoadName(0),
        ops.LoadName(1),
        ops.Call()
    ]
    assert frame.vars == [
        obj.LVar('b'),
        obj.LVar('print')
    ]


def test_do1(compile_stmt):
    frame = compile_stmt('do print(1) end')
