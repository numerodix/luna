import re

from parsimonious.nodes import NodeVisitor

from luna import ast


class Rewriter(NodeVisitor):
    def __init__(self, optable, *args, **kwargs):
        super(Rewriter, self).__init__(*args, **kwargs)
        self.optable = optable

    def generic_visit(self, node, vc):
        return vc


    def visit_program(self, node, vc):
        stmt, rest = vc
        if rest:
            rest = [s for (semi, ws, s) in rest]
            stmts = [stmt] + rest
            return ast.Program(*stmts)
        return ast.Program(stmt)


    def visit_stmt(self, node, vc):
        return ast.Stmt(vc[0])


    def visit_funccall(self, node, vc):
        id, ws, paren_open, args, paren_close = vc
        return ast.Call(id, args)

    def visit_funcargs(self, node, vc):
        expr, rest = vc
        if rest:
            rest = [e for (ws, comma, ws, e) in rest]
            expr = [expr] + rest
            return ast.Args(*expr)
        return ast.Args(expr)


    def visit_assignment(self, node, vc):
        id, ws, eq, ws, expr = vc
        return ast.Assignment(id, expr)


    def visit_expr(self, node, vc):
        return ast.Expr(*vc)

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

        # unwrap Expr if it only has an operand
        if type(expr.value) not in [ast.BinOp, ast.UnaryOp]:
            expr = expr.value

        # apply operator precedence
        elif type(expr.value) == ast.BinOp:
            op2 = expr.value.op

            if self.optable.level(op.value, 2) > self.optable.level(op2.value, 2):
                inner = ast.BinOp(factor, op, expr.value.left)
                outer = ast.BinOp(ast.Expr(inner), op2, expr.value.right)
                return outer

        return ast.BinOp(factor, op, expr)

    def visit_unop(self, node, vc):
        op, ws, expr = vc

        # unwrap Expr if it only has one value
        if type(expr.value) not in [ast.BinOp, ast.UnaryOp]:
            expr = expr.value

        # apply operator precedence
        elif type(expr.value) == ast.BinOp:
            op2 = expr.value.op

            if self.optable.level(op.value, 1) > self.optable.level(op2.value, 2):
                inner = ast.UnaryOp(op, expr.value.left)
                outer = ast.BinOp(ast.Expr(inner), op2, expr.value.right)
                return outer

        return ast.UnaryOp(op, expr)


    def visit_op1(self, node, vc):
        return ast.Operator(node.text)

    def visit_op2(self, node, vc):
        return ast.Operator(node.text)

    def visit_operand(self, node, vc):
        return vc[0]


    def visit_boolean(self, node, vc):
        return ast.Boolean(node.text)

    def visit_identifier(self, node, vc):
        return ast.Identifier(node.text)

    def visit_nil(self, node, vc):
        return ast.Nil()

    def visit_number(self, node, vc):
        return ast.Number(node.text)

    def visit_string(self, node, vc):
        s = node.text[1:-1]
        s = s.replace('\\"', '"')
        s = s.replace("\\'", "'")
        return ast.String(s)
