from luna.ast.base import ASTNode


class BinOp(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        assert len(values) == 3
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


class Expr(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class UnaryOp(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        assert len(values) == 2
        self.values = values

    @property
    def op(self):
        return self.values[1]

    @property
    def right(self):
        return self.values[2]
