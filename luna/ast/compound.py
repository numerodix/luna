from luna.ast.base import ASTNode


class Expr(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Infix(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values
