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

    def visit_concat_expr(self, node, vc):
        if len(vc) == 1:
            if type(vc[0]) == list:
                arith_expr, ws, op, ws, str_expr = vc[0]
                return ast.Concat(arith_expr, str_expr)
            return vc[0]

        raise Exception
        arith_expr, ws, op, ws, str_expr = vc
        return ast.Concat(arith_expr, op, str_expr)

    def visit_arith_expr(self, node, vc):
        term_expr, rest = vc
        if rest:
            rest = [(op, term_e) for (ws, op, ws, term_e) in rest]
            left = term_expr
            for op, term_e in rest:
                left = ast.Expr(ast.Arith(left, op, term_e))
            return left.value

        return term_expr

    def visit_term_expr(self, node, vc):
        unary_expr, rest = vc
        if rest:
            rest = [(op, unary_e) for (ws, op, ws, unary_e) in rest]
            left = unary_expr
            for op, unary_e in rest:
                left = ast.Expr(ast.Term(left, op, unary_e))
            return left.value

        return unary_expr

    def visit_unary_expr(self, node, vc):
        if len(vc) == 1:
            if type(vc[0]) == list:
                op, ws, power_expr = vc[0]
                return ast.UnaryOp(op, power_expr)
            return vc[0]

        raise Exception
        op, ws, power_expr = vc
        return ast.UnaryOp(op, power_expr)

    def visit_power_expr(self, node, vc):
        if len(vc) == 1:
            if type(vc[0]) == list:
                factor, ws, caret, ws, power_expr = vc[0]
                return ast.Power(factor, power_expr)
            return vc[0]

        raise Exception
        factor, ws, caret, ws, power_expr = vc
        return ast.Power(factor, caret, power_expr)

    def visit_factor(self, node, vc):
        if len(vc) == 1:
            return vc[0]

        paren, ws, expr, ws, paren = vc
        return expr


    # Operators

    def visit_cmp_op(self, node, vc):
        return ast.Operator(node.text)

    def visit_arith_op(self, node, vc):
        return ast.Operator(node.text)

    def visit_term_op(self, node, vc):
        return ast.Operator(node.text)

    def visit_unary_op(self, node, vc):
        return ast.Operator(node.text)

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
