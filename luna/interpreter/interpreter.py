from luna.ast.visitors import GenericVisitor


class EvalVisitor(GenericVisitor):
    def generic_visit(self, node, vc):
        return vc[0]

    def visit_call(self, node, vc):
        func, arg = vc
        return func(arg)

    def visit_expr(self, node, vc):
        return vc[0]

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
        return print if id == 'print' else None

    def visit_nil(self, node, vc):
        return None

    def visit_number(self, node, vc):
        return float(node.value)

    def visit_string(self, node, vc):
        return node.value
