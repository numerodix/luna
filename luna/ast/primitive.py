from luna.ast.base import ASTNode


class Boolean(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        if not value in ['true', 'false']:
            raise ValueError

        self.value = value


class Identifier(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Nil(ASTNode):
    pass


class Number(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class Operator(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value


class String(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value
