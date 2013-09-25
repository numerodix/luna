from luna.ast.base import ASTNode


class Args(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Assignment(ASTNode):
    _slots = ('identifier', 'expr')

    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr


class BinOp(ASTNode):
    _slots = ('left', 'op', 'right')

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Call(ASTNode):
    _slots = ('identifier', 'expr')

    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr


class Expr(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Program(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Stmt(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class UnaryOp(ASTNode):
    _slots = ('op', 'right')

    def __init__(self, op, right):
        self.op = op
        self.right = right
