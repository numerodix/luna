from luna.ast.base import ASTNode


class Expr(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values

    @property
    def left(self):
        return self.values[0]

    @property
    def op(self):
        return self.values[1]

    @property
    def right(self):
        return self.values[2]


class Infix(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values
