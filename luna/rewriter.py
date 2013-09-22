from parsimonious.nodes import NodeVisitor

from luna.ast import Boolean
from luna.ast import Nil


class Rewriter(NodeVisitor):
    def generic_visit(self, node, vc):
        return vc


    def visit_expr(self, node, vc):
        return vc[0]


    def visit_boolean(self, node, vc):
        return Boolean(node.text)

    def visit_nil(self, node, vc):
        return Nil()
