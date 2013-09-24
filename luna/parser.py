import re
import os

from parsimonious.grammar import Grammar

from luna.rewriter import Rewriter
from luna import util


class Parser(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'grammar.txt')
        content = util.read(fp)

        self.grammar = Grammar(content)
        optable = OperatorTable()
        self.rewriter = Rewriter(optable)

    def parse(self, content, rule=None):
        grammar = self.grammar
        if rule is not None:
            grammar = grammar[rule]

        tree = grammar.parse(content)
        tree = self.rewriter.visit(tree)
        return tree


class OperatorTable(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'operators.txt')
        content = util.read(fp)

        content = re.sub('#.*', '', content)
        lines = content.split('\n')

        idx = {}
        for i, line in enumerate(lines):
            for op in re.split('[ ]+', line):
                idx[op] = i

        self._idx = idx

    def level(self, op):
        return self._idx[op]


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-d', dest='dump', action="store_true")
    args = parser.parse_args()

    content = util.read(args.input)
    parser = Parser()
    tree = parser.parse(content)

    if args.dump:
        util.write(tree.pp())
    else:
        pp = prettyprinter.PP()
        util.write(pp.visit(tree))
