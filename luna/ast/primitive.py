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
    map = {
        '~=': '!=',
    }

    def __init__(self, value):
        self.value = value

    @property
    def pyvalue(self):
        pyop = self.map.get(self.value)
        return pyop or self.value


class String(ASTNode):
    _slots = ('value',)

    def __init__(self, value):
        self.value = value
