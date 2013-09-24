def test_eval_nums1(eval_expr):
    assert 2 == eval_expr('1 + 1')

def test_eval_nums2(eval_expr):
    assert 0 == eval_expr('1 - 1')

def test_eval_nums3(eval_expr):
    assert 0 == eval_expr('-1 + 1')

def test_eval_nums4(eval_expr):
    assert 7 == eval_expr('1 + 2 * 3')

def test_eval_nums5(eval_expr):
    assert 5 == eval_expr('1 * 2 + 3')


def test_eval_expr3(eval_expr):
    assert True == eval_expr('true')

def test_eval_expr4(eval_expr):
    assert True == eval_expr('true == true')

def test_eval_expr5(eval_expr):
    assert False == eval_expr('true ~= true')

def test_eval_expr6(eval_expr):
    assert False == eval_expr('not true')


def test_print1(exec_stmt, stdout):
    exec_stmt('print(1)')
    assert "1.0\n" == stdout()
