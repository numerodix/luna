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


class Block(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Call(ASTNode):
    _slots = ('identifier', 'expr')

    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr


class Expr(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Foreach(ASTNode):
    _slots = ('vars', 'exprs', 'block')

    def __init__(self, vars, exprs, block):
        self.vars = vars
        self.exprs = exprs
        self.block = block


class If(ASTNode):
    _slots = ('pred', 'thenblock', 'elseblock')

    def __init__(self, pred, thenblock, elseblock):
        self.pred = pred
        self.thenblock = thenblock
        self.elseblock = elseblock


class Program(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Repeat(ASTNode):
    _slots = ('block', 'expr')

    def __init__(self, block, expr):
        self.block = block
        self.expr = expr


class Stmt(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class UnaryOp(ASTNode):
    _slots = ('op', 'right')

    def __init__(self, op, right):
        self.op = op
        self.right = right


class While(ASTNode):
    _slots = ('expr', 'block')

    def __init__(self, expr, block):
        self.expr = expr
        self.block = block
