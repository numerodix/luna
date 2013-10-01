from luna import ast
from luna.ast.visitors import GenericVisitor
from luna.parser.operators import OperatorTable


class AssocRewriter(GenericVisitor):
    def __init__(self, optable):
        self.mutations = 0
        self.optable = optable

    @classmethod
    def fix(cls, optable, node):
        rewriter = cls(optable)

        rewriter.mutations = 1
        while rewriter.mutations > 0:
            rewriter.mutations = 0
            node = rewriter.visit(node)

        return node

    def generic_visit(self, node, vc):
        return node

    def visit_expr(self, node, vc):
        return ast.Expr(vc[0])

    def rewrite(self, factor, op, expr, op2):
        self.mutations += 1
        inner = ast.BinOp(factor, op, expr.value.left)
        outer = ast.BinOp(ast.Expr(inner), op2, expr.value.right)
        return outer

    def visit_binop(self, node, vc):
        factor, op, expr = node

        # don't rewrite if expr was in parens
        if type(expr.value) == ast.BinOp and not expr.parenthesized:
            op2 = expr.value.op

            if (op.value == op2.value
                and self.optable.assoc(op.value, 2) == OperatorTable.LEFT_ASSOC):
                return self.rewrite(factor, op, expr, op2)

            if self.optable.level(op.value, 2) > self.optable.level(op2.value, 2):
                return self.rewrite(factor, op, expr, op2)

        return node
