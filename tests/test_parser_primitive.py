from luna.ast import BinOp
from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Identifier
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator
from luna.ast import String
from luna.ast import UnaryOp


def test_nil(parse_operand):
    assert Nil() == parse_operand('nil')

def test_false(parse_operand):
    assert Boolean('false') == parse_operand('false')

def test_true(parse_operand):
    assert Boolean('true') == parse_operand('true')


def test_float1(parse_operand):
    assert Number('1') == parse_operand('1')

def test_float2(parse_operand):
    assert Number('1.') == parse_operand('1.')

def test_float3(parse_operand):
    assert Number('.1') == parse_operand('.1')


def test_string1(parse_operand):
    assert String("a'a") == parse_operand("'a\\'a'")

def test_string2(parse_operand):
    assert String('a"a') == parse_operand('"a\\"a"')
