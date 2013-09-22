from luna.ast import Boolean


def test_false(parser):
    assert parser.parse('false') == Boolean('false')

def test_true(parser):
    assert parser.parse('true') == Boolean('true')
