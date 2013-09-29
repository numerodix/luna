from luna import objects as obj
from luna.vm.opcodes import *


class Frame(object):
    def __init__(self, code, consts):
        self.code = code
        self.consts = consts

        self.stack = []

    def run(self):
        pc = 0
        stack = []

        while pc < len(self.code):
            op = self.code[pc]

            if type(op) == BinaryAdd:
                x = stack.pop(0)
                y = stack.pop(0)
                v = obj.LNumber(x.value + y.value)
                stack.append(v)

            elif type(op) == LoadConst:
                stack.append(self.consts[op.index])

            pc += 1

        return stack[0]
