class OpCode(object):
    _slots = tuple()

    # Equality

    def __eq__(self, other):
        # is the type equal?
        if not self.__class__ == other.__class__:
            return False

        my_children = [i for i in self]
        other_children = [i for i in other]

        # is child arity equal?
        if not len(my_children) == len(other_children):
            return False

        # are the children equal?
        pairs = zip(my_children, other_children)
        tests = [a == b for (a, b) in pairs]
        if not all(tests):
            return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    # Iterator

    def __iter__(self):
        for slot in self._slots:
            yield getattr(self, slot, None)

    # Representation

    def __repr__(self):
        children = [repr(i) for i in self]
        children = ', '.join(children)
        return '%s(%s)' % (
            self.__class__.__name__,
            children,
        )


class BinaryAdd(OpCode):
    pass

class BinarySubtract(OpCode):
    pass

class Call(OpCode):
    pass

class LoadConst(OpCode):
    _slots = ('index',)

    def __init__(self, index):
        self.index = index

class LoadName(OpCode):
    _slots = ('index',)

    def __init__(self, index):
        self.index = index

class StoreName(OpCode):
    _slots = ('index',)

    def __init__(self, index):
        self.index = index
