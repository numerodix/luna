import re
import os

from parsimonious.grammar import Grammar

from luna.parser.rewriter import Rewriter
from luna import util


class Parser(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'grammar.txt')
        content = util.read(fp)

        self.grammar = Grammar(content)
        optable = OperatorTable()
        self.rewriter = Rewriter(optable)

    def parse_with_rule(self, rule, content):
        grammar = self.grammar
        if rule is not None:
            grammar = grammar[rule]

        tree = grammar.parse(content)
        tree = self.rewriter.visit(tree)
        return tree

    def parse(self, content):
        return self.parse_with_rule(None, content)


class OperatorTable(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'operators.txt')
        content = util.read(fp)

        content = re.sub('#.*', '', content)
        lines = content.split('\n')
        lines = [line for line in lines if line]

        idx = {}
        for i, line in enumerate(lines):
            for op in re.split('[ ]+', line):
                op = op.strip()
                arity, op = op.split(':')

                arity = int(arity)
                level = len(lines) - i

                idx[(op, arity)] = level

        self._idx = idx

    def level(self, op, arity):
        return self._idx[(op, arity)]
