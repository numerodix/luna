import os

from parsimonious.grammar import Grammar

from luna.parser.operators import OperatorTable
from luna.parser.rewriter import Rewriter
from luna.parser.rewriter import BinopRewriter
from luna import util


class Parser(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'grammar.txt')
        content = util.read(fp)

        self.grammar = Grammar(content)
        self.optable = OperatorTable()
        self.rewriter = Rewriter(self.optable)
        self.binop = BinopRewriter(self.optable)

    def parse_with_rule(self, rule, content):
        grammar = self.grammar
        if rule is not None:
            grammar = grammar[rule]

        tree = grammar.parse(content)
        tree = self.rewriter.visit(tree)

        # apply operator precedence
        rewrites = 1
        while rewrites > 0:
            tree = self.binop.visit(tree)
            rewrites = self.binop.rewrites
            self.binop = BinopRewriter(self.optable)

        return tree

    def parse(self, content):
        return self.parse_with_rule(None, content)
