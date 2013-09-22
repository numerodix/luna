import pytest

from luna.parser import Parser


@pytest.fixture(scope='module')
def parser():
    return Parser()
