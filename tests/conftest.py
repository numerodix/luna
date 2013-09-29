from os.path import dirname
from os.path import join
import functools

import pytest

from luna import util
from luna.compiler import Compiler
from luna.parser import Parser


# Fixtures

@pytest.fixture(scope='function')
def stdout(capsys):
    def do():
        return capsys.readouterr()[0]
    return do


@pytest.fixture(scope='module')
def load_program():
    def do(filepath):
        base = join(dirname(dirname(__file__)), 'programs')
        fp = join(base, filepath)
        content = util.read(fp)
        return content
    return do


# Compilation

@pytest.fixture(scope='function')
def compile_program(parse_program):
    def do(program):
        tree = parse_program(program)
        compiler = Compiler()
        return compiler.compile(tree)
    return do

@pytest.fixture(scope='function')
def compile_stmt(parse_stmt):
    def do(program):
        tree = parse_stmt(program)
        compiler = Compiler()
        return compiler.compile(tree)
    return do

@pytest.fixture(scope='function')
def compile_expr(parse_expr):
    def do(program):
        tree = parse_expr(program)
        compiler = Compiler()
        return compiler.compile(tree)
    return do


# Interpretation

@pytest.fixture(scope='function')
def interp_program(compile_program):
    def do(program):
        frame = compile_program(program)
        return frame.run()
    return do

@pytest.fixture(scope='function')
def interp_stmt(compile_stmt):
    def do(program):
        frame = compile_stmt(program)
        return frame.run()
    return do

@pytest.fixture(scope='function')
def interp_expr(compile_expr):
    def do(program):
        frame = compile_expr(program)
        return frame.run()
    return do


# Parsing

@pytest.fixture(scope='module')
def parse_program():
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
