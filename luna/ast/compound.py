from luna.ast.base import ASTNode


class And(ASTNode):
    _slots = ('left', 'right')

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Args(ASTNode):
    _slots = ('values',)

    def __init__(self, *values):
        self.values = values


class Arith(ASTNode):
    _slots = ('left', 'op', 'right')

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


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


class Cmp(ASTNode):
    _slots = ('left', 'op', 'right')

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Concat(ASTNode):
    _slots = ('left', 'right')

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Do(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Expr(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Factor(ASTNode):
    _slots = ('value',)

    def __init__(self, *value):
        self.value = value


class For(ASTNode):
    _slots = ('var', 'low', 'high', 'step', 'block',)

    def __init__(self, var, low, high, step, block):
        self.var = var
        self.low = low
        self.high = high
        self.step = step
        self.block = block


class Foreach(ASTNode):
    _slots = ('vars', 'exprs', 'block')

    def __init__(self, vars, exprs, block):
        self.vars = vars
        self.exprs = exprs
        self.block = block


class Funcdef(ASTNode):
    _slots = ('name', 'params', 'block')

    def __init__(self, name, params, block):
        self.name = name
        self.params = params
        self.block = block


class If(ASTNode):
    _slots = ('pred', 'thenblock', 'elseblock')

    def __init__(self, pred, thenblock, elseblock):
        self.pred = pred
        self.thenblock = thenblock
        self.elseblock = elseblock


class Power(ASTNode):
    _slots = ('left', 'right')

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Program(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Operand(ASTNode):
    _slots = ('value',)

    def __init__(self, *value):
        self.value = value


class Or(ASTNode):
    _slots = ('left', 'right')

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Repeat(ASTNode):
    _slots = ('block', 'expr')

    def __init__(self, block, expr):
        self.block = block
        self.expr = expr


class Return(ASTNode):
    _slots = ('expr',)

    def __init__(self, expr):
        self.expr = expr


class SeqOp(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Stmt(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Term(ASTNode):
    _slots = ('left', 'op', 'right')

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


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
