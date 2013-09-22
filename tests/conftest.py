import pytest

from luna.parser import Parser


@pytest.fixture(scope='module')
def parse():
    parser = Parser()
    return parser.parse
