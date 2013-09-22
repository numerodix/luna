from luna.ast import Boolean
from luna.ast import Nil


def test_nil(parser):
    assert parser.parse('nil') == Nil()

def test_false(parser):
    assert parser.parse('false') == Boolean('false')

def test_true(parser):
    assert parser.parse('true') == Boolean('true')
