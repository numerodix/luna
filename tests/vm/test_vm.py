

def test_binop(compile_expr):
    frame = compile_expr('1 + 2')
    top = frame.run()
    assert 3 == top.value
