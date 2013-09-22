from functools import reduce

from parsimonious.nodes import NodeVisitor

from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Infix
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator


class Rewriter(NodeVisitor):
    def generic_visit(self, node, vc):
        return vc


    def visit_expr(self, node, vc):
        return Expr(*vc)

    def visit_infix(self, node, vc):
        a, _, op, _, b, rest = vc
        args = [a, op, b]
        if rest:
            rest = [[a, b] for (_, a, _, b) in rest]
            rest = reduce(lambda a,b: a + b, rest)
            args = args + rest
        return Infix(*args)


    def visit_operator(self, node, vc):
        return Operator(node.text)

    def visit_operand(self, node, vc):
        return vc[0]


    def visit_boolean(self, node, vc):
        return Boolean(node.text)

    def visit_nil(self, node, vc):
        return Nil()

    def visit_number(self, node, vc):
        return Number(node.text)
