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
                v = obj.LNumber(y.value + x.value)
                self.stack.insert(0, v)

            elif type(op) == ops.BinarySubtract:
                x = self.stack.pop(0)
                y = self.stack.pop(0)
                v = obj.LNumber(y.value - x.value)
                self.stack.insert(0, v)

            elif type(op) == ops.Call:
                arg = self.stack.pop(0)
                funcname = self.stack.pop(0)
                if type(arg) == obj.LVar:
                    arg = self.env[arg]
                func = getattr(builtin, 'lua_' + funcname.value)
                func(arg)

            elif type(op) == ops.LoadConst:
                self.stack.insert(0, self.consts[op.index])

            elif type(op) == ops.StoreName:
                val = self.stack.pop(0)
                var = self.stack.pop(0)
                self.env[var] = val

            self.pc += 1

        return self
