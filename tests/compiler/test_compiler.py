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
        obj.LString('a'),
        obj.LNumber(1.0),
    ]


def test_binop1(compile_expr):
    frame = compile_expr('1 + 2')

    assert frame.code == [
        ops.LoadConst(0),
        ops.LoadConst(1),
        ops.BinaryAdd(),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
    ]
