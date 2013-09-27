import six


class ASTNode(object):
    _slots = tuple()

    # Equality

    def __lenient_eq(self, a, b):
        '''Compare a and b. If either is Lazy it will succeed.'''

        if type(b) == Lazy:
            return b == a

        return a == b

    def __eq__(self, other):
        # succeed early if we found Lazy, no need to recurse
        if type(self) == Lazy or type(other) == Lazy:
            return True

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
        tests = [self.__lenient_eq(a, b) for (a, b) in pairs]
        if not all(tests):
            return False

        return True

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

    def pp(self, tabsize=2):
        def dotab(s, indent):
            tab = ' ' * indent * tabsize
            ss = s.split('\n')
            ss = ['%s%s' % (tab, s) for s in ss]
            return '\n'.join(ss)

        def rec(node, indent):
            if (node is None
                or type(node) in [int]
                or isinstance(node, six.string_types)):
                return repr(node)

            children = [rec(ch, indent) for ch in node]

            s_children = ''
            if children:
                children = [dotab(ch, indent+1) for ch in children]
                children = ',\n'.join(children)
                s_children = '\n' + children + '\n'

            fmt = '%(prefix)s(%(children)s%(suffix)s' % {
                'children': s_children,
                'prefix': node.__class__.__name__,
                'suffix': ')',
            }

            return fmt

        return rec(self, 0)


class Lazy(ASTNode):
    '''This class is used in the place of a subgraph when we don't want
    to specify the tree to match in full. It will always be equal
    to whatever node it's being compared to.'''

    def __eq__(self, other):
        return True


class Empty(ASTNode):
    _slots = tuple()
