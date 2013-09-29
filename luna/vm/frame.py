from luna import objects as obj
from luna.stdlib import builtin
from luna.vm import opcodes as ops


class Frame(object):
    def __init__(self, code, consts):
        self.code = code
        self.consts = consts

        self.pc = 0
        self.env = {}
        self.stack = []

    def run(self):
        while self.pc < len(self.code):
            op = self.code[self.pc]

            if type(op) == ops.BinaryAdd:
                x = self.stack.pop(0)
                y = self.stack.pop(0)
                v = obj.LNumber(x.value + y.value)
                self.stack.append(v)

            elif type(op) == ops.Call:
                x = self.stack.pop(0)
                y = self.stack.pop(0)
                if type(y) == obj.LVar:
                    y = self.env[y]
                func = getattr(builtin, 'lua_' + x.value)
                func(y)

            elif type(op) == ops.LoadConst:
                self.stack.append(self.consts[op.index])

            elif type(op) == ops.StoreName:
                x = self.stack.pop(0)
                y = self.stack.pop(0)
                self.env[x] = y

            self.pc += 1

        return self
