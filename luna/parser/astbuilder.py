import re

from parsimonious.nodes import NodeVisitor

from luna import ast


class AstBuilder(NodeVisitor):
    def __init__(self, optable, *args, **kwargs):
        self.optable = optable

    def generic_visit(self, node, vc):
        return vc

    
    # Expressions

    def visit_expr(self, node, vc):
        [value] = vc
        return ast.Expr(value)

    def visit_or_expr(self, node, vc):
        and_expr, rest = vc
        if rest:
            pass  # TODO
        return and_expr

    def visit_and_expr(self, node, vc):
        cmp_expr, rest = vc
        if rest:
            pass  # TODO
        return cmp_expr

    def visit_cmp_expr(self, node, vc):
        str_expr, rest = vc
        if rest:
            pass  # TODO
        return str_expr

    def visit_str_expr(self, node, vc):
        if len(vc) == 1:
            return vc[0]

        arith_expr, ws, op, ws, str_expr = vc
        return ast.StrOp(arith_expr, op, str_expr)

    def visit_arith_expr(self, node, vc):
        term_expr, rest = vc
        if rest:
            pass  # TODO
        return term_expr

    def visit_term_expr(self, node, vc):
        unary_expr, rest = vc
        if rest:
            pass   # TODO
        return unary_expr

    def visit_unary_expr(self, node, vc):
        if len(vc) == 1:
            return vc[0]

        op, ws, power_expr = vc
        return ast.UnaryOp(op, power_expr)

    def visit_power_expr(self, node, vc):
        if len(vc) == 1:
            return vc[0]

        factor, ws, caret, ws, power_expr = vc
        return ast.Power(factor, caret, power_expr)

    def visit_factor(self, node, vc):
        if len(vc) == 1:
            return vc[0]

        paren, ws, expr, ws, paren = vc
        return expr


    # Operators

    def visit_cmp_op(self, node, vc):
        return node.text

    def visit_arith_op(self, node, vc):
        return node.text

    def visit_term_op(self, node, vc):
        return node.text

    def visit_unary_op(self, node, vc):
        return node.text

    def visit_operand(self, node, vc):
        return vc[0]


    # Atoms

    def visit_string(self, node, vc):
        s = node.text[1:-1]
        s = s.replace('\\"', '"')
        s = s.replace("\\'", "'")
        return ast.String(s)

    def visit_number(self, node, vc):
        return ast.Number(node.text)

    def visit_identifier(self, node, vc):
        return ast.Identifier(node.text)

    def visit_boolean(self, node, vc):
        return ast.Boolean(node.text)

    def visit_nil(self, node, vc):
        return ast.Nil()
