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
