import os
import re

from luna import util


class OperatorTable(object):
    LEFT_ASSOC = 0
    RIGHT_ASSOC = 1

    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(dir, 'operators.txt')
        content = util.read(fp)

        content = re.sub(';.*', '', content)
        lines = content.split('\n')
        lines = [line for line in lines if line]

        idx = {}
        for i, line in enumerate(lines):
            for op in re.split('[ ]+', line):
                op = op.strip()
                arity, assoc, op = op.split(':')

                arity = int(arity)
                level = len(lines) - i

                assoc = (self.LEFT_ASSOC
                         if assoc.lower() == 'l'
                         else self.RIGHT_ASSOC)

                idx[(op, arity)] = (level, assoc)

        self._idx = idx

    def assoc(self, op, arity):
        (level, assoc) = self._idx[(op, arity)]
        return assoc

    def level(self, op, arity):
        (level, assoc) = self._idx[(op, arity)]
        return level
