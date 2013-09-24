def test_eval_expr1(eval_expr):
    assert 2 == eval_expr('1 + 1')

def test_eval_expr2(eval_expr):
    assert 0 == eval_expr('1 - 1')
