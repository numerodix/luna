from luna import ast
from luna.ast.visitors import GenericVisitor


class EvalVisitor(GenericVisitor):
    def __init__(self, env):
        self.env = env

    def generic_visit(self, node, vc):
        if vc:
            vc = vc[0]
        return vc


    def visit_expr(self, node, vc):
        return vc[0]

    def visit_call(self, node, vc):
        func, arg = vc

        # if it's coming from the env it's not eval'd yet
        if isinstance(arg, ast.ASTNode):
            arg = self.visit(arg)

        # print float as int if it's an int
        if type(arg) == float and arg == int(arg):
            arg = int(arg)

        if callable(func):
            return func(arg)

    def visit_binop(self, node, vc):
        left, op, right = list(vc)
        return eval('%s %s %s' % (left, op, right))

    def visit_unaryop(self, node, vc):
        op, right = list(vc)
        return eval('%s %s' % (op, right))


    def visit_operator(self, node, vc):
        return node.pyvalue

    def visit_boolean(self, node, vc):
        return True if node.value == 'true' else False

    def visit_identifier(self, node, vc):
        [id] = vc
        return self.env[id]

    def visit_nil(self, node, vc):
        return None

    def visit_number(self, node, vc):
        return float(node.value)

    def visit_string(self, node, vc):
        return node.value
