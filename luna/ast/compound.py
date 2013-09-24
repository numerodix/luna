from luna.ast.base import ASTNode


class BinOp(ASTNode):
    _slots = ('left', 'op', 'right')

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Expr(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class UnaryOp(ASTNode):
    _slots = ('op', 'right')

    def __init__(self, op, right):
        self.op = op
        self.right = right
