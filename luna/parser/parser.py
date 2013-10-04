import os

from parsimonious.grammar import Grammar

from luna.parser.operators import OperatorTable
from luna.parser.assoc import AssocRewriter
from luna.parser.astbuilder import AstBuilder
from luna.parser.astbuilder import prune
from luna import util


class Parser(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'grammar.txt')
        content = util.read(fp)

        self.grammar = Grammar(content)
        self.optable = OperatorTable()
        self.builder = AstBuilder(self.optable)

    def parse_with_rule(self, rule, content):
        grammar = self.grammar
        if rule is not None:
            grammar = grammar[rule]

        tree = grammar.parse(content)
        tree = self.builder.visit(tree)

        return tree

    def parse(self, content):
        return self.parse_with_rule(None, content)
