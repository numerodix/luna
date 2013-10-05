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
                x = self.stack.pop()
                y = self.stack.pop()
                v = obj.LNumber(y.value + x.value)
                self.stack.append(v)

            elif type(op) == ops.BinarySubtract:
                x = self.stack.pop()
                y = self.stack.pop()
                v = obj.LNumber(y.value - x.value)
                self.stack.append(v)

            elif type(op) == ops.Call:
                funcname = self.stack.pop()
                arg = self.stack.pop()
                if type(arg) == obj.LVar:
                    arg = self.env[arg]
                func = getattr(builtin, 'lua_' + funcname.value)
                func(arg)

            elif type(op) == ops.LoadConst:
                self.stack.append(self.consts[op.index])

            elif type(op) == ops.LoadName:
                self.stack.append(self.env[op.index])

            elif type(op) == ops.StoreName:
                var = self.stack.pop()
                val = self.stack.pop()
                if type(val) == obj.LVar:
                    val = self.env[val]
                self.env[var] = val

            self.pc += 1

        return self
