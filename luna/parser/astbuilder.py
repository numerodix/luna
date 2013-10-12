import re

from parsimonious.nodes import NodeVisitor

from luna import ast


class AstBuilder(NodeVisitor):
    def generic_visit(self, node, vc):
        return vc


    # Program

    def visit_program(self, node, vc):
        ws, block = vc
        return ast.Program(block)

    def visit_block(self, node, vc):
        stmts = vc
        stmts = [stmt for stmt in stmts if not type(stmt) == ast.SeqOp]
        return ast.Block(*stmts)


    # Statements

    def visit_stmt(self, node, vc):
        value = vc[0]
        if type(value) == ast.SeqOp:
            return value
        return ast.Stmt(value)

    def visit_do(self, node, vc):
        do, ws, block, ws, end = vc
        return ast.Do(block)

    def visit_assignment(self, node, vc):
        id, ws, op, ws, expr = vc
        return ast.Assignment(id, expr)

    def visit_seq_op(self, node, vc):
        return ast.SeqOp(node.text.strip())

    
    # Expressions

    def visit_expr(self, node, vc):
        [value] = vc
        return ast.Expr(value)

    def visit_or_expr(self, node, vc):
        and_expr, rest = vc
        if rest:
            rest = [and_e for (ws, op, ws, and_e) in rest]
            left = and_expr
            for and_e in rest:
                left = ast.Or(left, and_e)
            return left

        return and_expr

    def visit_and_expr(self, node, vc):
        cmp_expr, rest = vc
        if rest:
            rest = [cmp_e for (ws, op, ws, cmp_e) in rest]
            left = cmp_expr
            for cmp_e in rest:
                left = ast.And(left, cmp_e)
            return left

        return cmp_expr

    def visit_cmp_expr(self, node, vc):
        concat_expr, rest = vc
        if rest:
            rest = [(op, concat_e) for (ws, op, ws, concat_e) in rest]
            left = concat_expr
            for op, concat_e in rest:
                left = ast.Cmp(left, op, concat_e)
            return left

        return concat_expr

    def visit_concat_expr(self, node, vc):
        [vc] = vc
        if type(vc) == list:
            arith_expr, ws, op, ws, concat_expr = vc
            return ast.Concat(arith_expr, concat_expr)

        return vc

    def visit_arith_expr(self, node, vc):
        term_expr, rest = vc
        if rest:
            rest = [(op, term_e) for (ws, op, ws, term_e) in rest]
            left = term_expr
            for op, term_e in rest:
                left = ast.Arith(left, op, term_e)
            return left

        return term_expr

    def visit_term_expr(self, node, vc):
        unary_expr, rest = vc
        if rest:
            rest = [(op, unary_e) for (ws, op, ws, unary_e) in rest]
            left = unary_expr
            for op, unary_e in rest:
                left = ast.Term(left, op, unary_e)
            return left

        return unary_expr

    def visit_unary_expr(self, node, vc):
        [vc] = vc
        if type(vc) == list:
            op, ws, power_expr = vc
            return ast.UnaryOp(op, power_expr)

        return vc

    def visit_power_expr(self, node, vc):
        [vc] = vc
        if type(vc) == list:
            factor, ws, caret, ws, power_expr = vc
            return ast.Power(factor, power_expr)

        return vc

    def visit_factor(self, node, vc):
        [vc] = vc
        if type(vc) == list:
            paren, ws, expr, ws, paren = vc
            return expr

        return vc


    # Funccalls

    def visit_funcall(self, node, vc):
        id, ws, paren, ws, args, ws, paren = vc
        return ast.Call(id, args[0] or None)

    def visit_funargs(self, node, vc):
        expr, rest = vc
        if rest:
            rest = [e for (ws, comma, ws, e) in rest]
            expr = [expr] + rest

        return ast.Args(*expr)


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
