from luna import objects as obj
from luna.vm import opcodes as op


def test_binop(compile_expr):
    frame = compile_expr('1 + 2')

    assert frame.code == [
        op.LoadConst(0),
        op.LoadConst(1),
        op.BinaryAdd(),
    ]
    assert frame.consts == [
        obj.LNumber(1.0),
        obj.LNumber(2.0),
    ]
