from luna.ast.visitors import GenericVisitor


class EvalVisitor(GenericVisitor):
    def visit_print(self, node, vc):
        val = vc[0]
        print(val)

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

    def visit_nil(self, node, vc):
        return None

    def visit_number(self, node, vc):
        return float(node.value)

    def visit_string(self, node, vc):
        return node.value
