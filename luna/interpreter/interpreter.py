from luna.ast.visitors import GenericVisitor


class EvalVisitor(GenericVisitor):
    def visit_expr(self, node, vc):
        return vc[0]

    def visit_binop(self, node, vc):
        left, op, right = list(vc)
        return eval('%s %s %s' % (left, op, right))

    def visit_operator(self, node, vc):
        return node.value

    def visit_number(self, node, vc):
        return float(node.value)
