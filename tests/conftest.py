import functools

import pytest

from luna.parser import Parser


@pytest.fixture(scope='module')
def parse():
    parser = Parser()
    return parser.parse

@pytest.fixture(scope='module')
def parse_expr():
    parser = Parser()
    return functools.partial(parser.parse_with_rule, 'expr')

@pytest.fixture(scope='module')
def parse_operand():
    parser = Parser()
    return functools.partial(parser.parse_with_rule, 'operand')
