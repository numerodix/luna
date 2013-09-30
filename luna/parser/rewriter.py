import re

from parsimonious.nodes import NodeVisitor

from luna import ast
from luna.parser import OperatorTable


class Rewriter(NodeVisitor):
    def __init__(self, optable, *args, **kwargs):
        super(Rewriter, self).__init__(*args, **kwargs)
        self.optable = optable

    def generic_visit(self, node, vc):
        return vc


    def visit_program(self, node, vc):
        block, newline = vc
        return ast.Program(block)


    def visit_block(self, node, vc):
        stmt, rest = vc
        if rest:
            rest = [s for (semi, ws, s) in rest]
            stmts = [stmt] + rest
            return ast.Block(*stmts)
        return ast.Block(stmt)

    def visit_stmt(self, node, vc):
        return ast.Stmt(vc[0])


    def visit_if(self, node, vc):
        ifkw, ws, expr, ws, thenkw, ws, thenblock, ws, elifblocks, elseblock, end = vc

        if elseblock:
            elsekw, ws, elseblock, ws = elseblock[0]
        else:
            elseblock = ast.Empty()

        if elifblocks:
            elifblocks = [(e, b) for (elseifkw, ws, e, ws, thenkw, ws, b, ws)
                          in elifblocks]
            elifblocks.reverse()

            inner_if = elseblock
            for (ex, th) in elifblocks:
                inner_if = ast.If(ex, th, inner_if)

            elseblock = inner_if

        return ast.If(expr, thenblock, elseblock)

    def visit_for(self, node, vc):
        [forkw, ws, id, ws, eqkw, ws,
         low, ws, comma, ws, high, ws, step,
         dokw, ws, block, ws, endkw] = vc

        if step:
            comma, ws, step, ws = step[0]
        else:
            step = ast.Empty()

        return ast.For(id, low, high, step, block)

    def visit_foreach(self, node, vc):
        [forkw, ws, id, ids, ws,
         inkw, ws, expr, exprs, ws,
         dokw, ws, block, ws, endkw] = vc

        if ids:
            ids = [i for (ws, comma, ws, i) in ids]
            ids = [id] + ids

        if exprs:
            exprs = [e for (ws, comma, ws, e) in exprs]
            exprs = [expr] + exprs

        return ast.Foreach(ids, exprs, block)

    def visit_funcdef(self, node, vc):
        [funkw, ws, name, ws,
         paren, ws, params, ws, paren, ws,
         block, ws, endkw] = vc

        if params:
            params = params[0]
        else:
            params = ast.Empty()

        return ast.Funcdef(name, params, block)

    def visit_funcparams(self, node, vc):
        expr, rest = vc
        if rest:
            rest = [e for (ws, comma, ws, e) in rest]
            expr = [expr] + rest
            return expr
        return [expr]

    def visit_repeat(self, node, vc):
        repeat, ws, block, ws, until, ws, expr = vc
        return ast.Repeat(block, expr)

    def visit_return(self, node, vc):
        retkw, ws, expr = vc
        return ast.Return(expr)

    def visit_while(self, node, vc):
        whil, ws, expr, ws, do, ws, block, ws, end = vc
        return ast.While(expr, block)

    def visit_funccall(self, node, vc):
        id, ws, paren_open, ws, args, ws, paren_close = vc
        if args:
            args = args[0]
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

            if (op.value == op2.value
                and self.optable.assoc(op.value, 2) == OperatorTable.LEFT_ASSOC):
                inner = ast.BinOp(factor, op, expr.value.left)
                outer = ast.BinOp(ast.Expr(inner), op2, expr.value.right)
                return ast.BinOp(expr, op, factor)

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
