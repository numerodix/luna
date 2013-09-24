import functools

import pytest

from luna.parser import Parser
from luna.interpreter import EvalVisitor


@pytest.fixture(scope='module')
def eval_expr(parse_expr):
    visitor = EvalVisitor()
    def do(program):
        node = parse_expr(program)
        return visitor.visit(node)
    return do


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
