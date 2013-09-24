def test_eval_expr1(eval_expr):
    assert 2 == eval_expr('1 + 1')

def test_eval_expr2(eval_expr):
    assert 0 == eval_expr('1 - 1')


def test_eval_expr3(eval_expr):
    assert True == eval_expr('true')

def test_eval_expr4(eval_expr):
    assert True == eval_expr('true == true')

def test_eval_expr5(eval_expr):
    assert False == eval_expr('true ~= true')

def test_eval_expr6(eval_expr):
    assert False == eval_expr('not true')
