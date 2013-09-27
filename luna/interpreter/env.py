from luna.ast.visitors import GenericVisitor


class EnvBuilder(GenericVisitor):
    def __init__(self):
        self.env = {}

    def generic_visit(self, node, vc):
        pass

    def visit_funcdef(self, node, vc):
        self.env[node.name.value] = node

    def visit_assignment(self, node, vc):
        self.env[node.identifier.value] = node.expr
