from unittest import TestCase

from luna.parser import Parser
from luna.ast import Boolean


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_true(self):
        code = 'true'

        ast = self.parser.parse(code)

        assert ast == Boolean('true')
