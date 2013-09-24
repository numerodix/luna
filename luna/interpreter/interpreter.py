class GenericVisitor(object):
    def visit(self, node):
        clsname = node.__class__.__name__.lower()
        method = getattr(self, 'visit_%s' % clsname, None)

        if method:
            return method(node)
        else:
            self.generic_visit(node)

    def generic_visit(self, node):
        return vc


class EvalVisitor(GenericVisitor):
    def visit_expr(self, node):
        return self.visit_binop(node.value)

    def visit_binop(self, node):
        left, op, right = list(node)
        left = self.visit_number(left)
        op = self.visit_operator(op)
        right = self.visit_number(right)
        return eval('%s %s %s' % (left, op, right))

    def visit_operator(self, node):
        return node.value

    def visit_number(self, node):
        return float(node.value)
