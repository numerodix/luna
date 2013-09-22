import os

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

from luna.ast import Boolean
from luna import util


class Parser(object):
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'grammar.txt')
        content = util.read(fp)

        self.grammar = Grammar(content)
        self.rewriter = Rewriter()

    def parse(self, content):
        tree = self.grammar.parse(content)
        tree = self.rewriter.visit(tree)
        return tree


class Rewriter(NodeVisitor):
    def generic_visit(self, node, vc):
        return vc

    def visit_boolean(self, node, vc):
        return Boolean(node.text)



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

