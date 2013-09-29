from luna.ast import *


def test_expr_unary1(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('not'),
            Boolean('true'),
        ),
    ) == parse_expr('not true')

def test_expr_unary2(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('not'),
            Expr(
                UnaryOp(
                    Operator('not'),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('not not true')


def test_expr_eq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('true == true')

def test_expr_neq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
        ),
    ) == parse_expr('true ~= true')


def test_expr_paren1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('( true == true ) == true')

def test_expr_paren2(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('true == ( true == true )')


def test_expr_ternary(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('true == true == true')

def test_expr_quaternary(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Expr(
                        BinOp(
                            Boolean('true'),
                            Operator('=='),
                            Boolean('true'),
                        ),
                    ),
                ),
            ),
        ),
    ) == parse_expr('true == true == true == true')


def test_expr_nums1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('1'),
                    Operator('*'),
                    Number('2'),
                ),
            ),
            Operator('+'),
            Number('3'),
        ),
    ) == parse_expr('1 * 2 + 3')

def test_expr_nums2(parse_expr):
    assert Expr(
        BinOp(
            Number('1'),
            Operator('+'),
            Expr(
                BinOp(
                    Number('2'),
                    Operator('*'),
                    Number('3'),
                ),
            ),
        ),
    ) == parse_expr('1 + 2 * 3')

def test_expr_nums3(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                UnaryOp(
                    Operator('-'),
                    Number('1'),
                ),
            ),
            Operator('+'),
            Number('1'),
        ),
    ) == parse_expr('-1 + 1')

def test_expr_nums4(parse_expr):
    assert Expr(
        BinOp(
            Identifier('a'),
            Operator('+'),
            Number('1'),
        ),
    ) == parse_expr('a + 1')


def test_expr_call1(parse_expr):
    assert Expr(
        Call(
            Identifier('print'),
            Args(Lazy()),
        ),
    ) == parse_expr('print(x)')
