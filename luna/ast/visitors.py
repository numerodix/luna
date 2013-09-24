import six


class GenericVisitor(object):
    def visit(self, node):
        if isinstance(node, six.string_types):
            return node

        clsname = node.__class__.__name__.lower()
        method = getattr(self, 'visit_%s' % clsname, self.generic_visit)

        vc = [self.visit(c) for c in node]
        return method(node, vc)

    def generic_visit(self, node, vc):
        raise NotImplementedError
