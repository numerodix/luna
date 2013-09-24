import re

from parsimonious.nodes import NodeVisitor

from luna.ast import BinOp
from luna.ast import Boolean
from luna.ast import Expr
from luna.ast import Identifier
from luna.ast import Nil
from luna.ast import Number
from luna.ast import Operator
from luna.ast import String
from luna.ast import UnaryOp


class Rewriter(NodeVisitor):
    def __init__(self, optable, *args, **kwargs):
        super(Rewriter, self).__init__(*args, **kwargs)
        self.optable = optable

    def generic_visit(self, node, vc):
        return vc


    def visit_expr(self, node, vc):
        return Expr(*vc)

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

    def visit_binop(self, node, vc):
        factor, ws, op, ws, expr = vc

        # unwrap Expr if it only has one value
        if type(expr.value) not in [BinOp, UnaryOp]:
            expr = expr.value

        # apply operator precedence
        if type(expr.value) == BinOp:
            op2 = expr.value.op

            if self.optable.level(op.value) < self.optable.level(op2.value):
                inner = BinOp(factor, op, expr.value.left)
                outer = BinOp(Expr(inner), op2, expr.value.right)
                return outer

        return BinOp(factor, op, expr)

    def visit_unop(self, node, vc):
        op, ws, expr = vc
        return UnaryOp(factor, op, expr)


    def visit_op2(self, node, vc):
        return Operator(node.text)

    def visit_operand(self, node, vc):
        return vc[0]


    def visit_boolean(self, node, vc):
        return Boolean(node.text)

    def visit_identifier(self, node, vc):
        return Identifier(node.text)

    def visit_nil(self, node, vc):
        return Nil()

    def visit_number(self, node, vc):
        return Number(node.text)

    def visit_string(self, node, vc):
        s = node.text[1:-1]
        s = s.replace('\\"', '"')
        s = s.replace("\\'", "'")
        return String(s)
