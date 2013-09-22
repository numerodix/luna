from parsimonious.nodes import NodeVisitor

from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Nil
from luna.ast import Operator


class Rewriter(NodeVisitor):
    def generic_visit(self, node, vc):
        return vc


    def visit_expr(self, node, vc):
        try:
            a, _, op, _, b = vc[0]
            return Expr(a, op, b)
        except ValueError:
            pass
        return Expr(*vc)


    def visit_operator(self, node, vc):
        return Operator(node.text)

    def visit_operand(self, node, vc):
        return vc[0]

    def visit_boolean(self, node, vc):
        return Boolean(node.text)

    def visit_nil(self, node, vc):
        return Nil()
