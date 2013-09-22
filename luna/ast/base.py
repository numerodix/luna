import six


class ASTNode(object):
    _slots = tuple()

    # Equality

    def __eq__(self, other):
        if not self.__class__ == other.__class__:
            return False

        pairs = zip([i for i in self], [i for i in other])
        tests = [(a == b) for (a, b) in pairs]
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
