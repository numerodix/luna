from luna import ast
from luna.ast.visitors import GenericVisitor
from luna.parser.operators import OperatorTable


class AssocRewriter(GenericVisitor):
    def __init__(self, optable):
        self.optable = optable

    @classmethod
    def fix(cls, optable, node):
        rewriter = cls(optable)

        node_prev = None
        while node != node_prev:
            node_prev = node
            node = rewriter.visit(node)

        return node

    def generic_visit(self, node, vc):
        return node

    def visit_expr(self, node, vc=None):
        if type(node.value) == ast.BinOp:
            node.value = self.visit_binop(node.value)
        return node

    def visit_binop(self, node, vc=None):
        factor, op, expr = node

        # don't rewrite if expr was in parens
        if type(expr.value) == ast.BinOp and not expr.parenthesized:
            op2 = expr.value.op

            if self.optable.level(op.value, 2) > self.optable.level(op2.value, 2):
                node = self.rewrite(factor, op, self.visit_expr(expr), op2)

            elif (op.value == op2.value
                and self.optable.assoc(op.value, 2) == OperatorTable.LEFT_ASSOC):
                node = self.rewrite(factor, op, self.visit_expr(expr), op2)

        return node

    def rewrite(self, factor, op, expr, op2):
        inner = ast.BinOp(factor, op, expr.value.left)
        outer = ast.BinOp(ast.Expr(inner), op2, expr.value.right)
        return outer
