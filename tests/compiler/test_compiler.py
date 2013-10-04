from luna import objects as obj
from luna.vm import opcodes as ops


def test_ass1(compile_stmt):
    frame = compile_stmt('a = 1')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.StoreName(),
    ]
    assert frame.consts == [
        obj.LVar('a'),
        obj.LNumber(1.0),
    ]

def test_ass2(compile_stmt):
    frame = compile_stmt('a = 1 - 2')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.BinarySubtract(),
        ops.LoadConst(2),
        ops.StoreName(),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
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
