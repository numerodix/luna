import functools

import pytest

from luna.parser import Parser
from luna.interpreter import interpret


@pytest.fixture(scope='function')
def stdout(capsys):
    def do():
        return capsys.readouterr()[0]
    return do


@pytest.fixture(scope='module')
def exec_stmt(parse_stmt):
    def do(program):
        node = parse_stmt(program)
        return interpret(node)
    return do

@pytest.fixture(scope='module')
def eval_expr(parse_expr):
    def do(program):
        node = parse_expr(program)
        return interpret(node)
    return do


@pytest.fixture(scope='module')
def parse():
    parser = Parser()
    return parser.parse

@pytest.fixture(scope='module')
def parse_stmt():
    parser = Parser()
    return functools.partial(parser.parse_with_rule, 'stmt')

@pytest.fixture(scope='module')
def parse_expr():
    parser = Parser()
    return functools.partial(parser.parse_with_rule, 'expr')

@pytest.fixture(scope='module')
def parse_operand():
    parser = Parser()
    return functools.partial(parser.parse_with_rule, 'operand')
