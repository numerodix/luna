from functools import reduce

from parsimonious.nodes import NodeVisitor

from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Infix
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator


class Rewriter(NodeVisitor):
    def __init__(self, optable, *args, **kwargs):
        super(Rewriter, self).__init__(*args, **kwargs)
        self.optable = optable

    def generic_visit(self, node, vc):
        return vc


    def visit_expr(self, node, vc):
        args = []
        # factor
        if node.children[0].expr_name == 'factor':
            args = vc

        # ( ( factor ws operator ws expr ) ( operator expr )* )
        else:
            factor, ws, op, ws, expr = vc[0]

            # unwrap Expr if it only has one value
            if len(expr.values) == 1:
                expr = expr.values[0]

            # apply operator precedence
            if type(expr) == Expr:
                op2 = expr.op

                if self.optable.level(op.value) < self.optable.level(op2.value):
                    inner = Expr(factor, op, expr.left)
                    outer = Expr(inner, op2, expr.right)
                    return outer

            args = [factor, op, expr]

        return Expr(*args)

    def visit_factor(self, node, vc):
        args = []

        # operand
        if node.children[0].expr_name == 'operand':
            args = vc[0]

        # ( expr )
        else:
            paren, ws, expr, ws, paren = vc[0]
            args = expr

        return args

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
