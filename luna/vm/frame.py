from luna import objects as obj
from luna.stdlib import builtin
from luna.vm import opcodes as ops


class Frame(object):
    def __init__(self, code, consts, vars):
        self.code = code
        self.consts = consts
        self.vars = vars

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
                func = self.stack.pop()
                arg = self.stack.pop()
                if type(arg) == obj.LVar:
                    arg = self.env[arg]
                func(arg)

            elif type(op) == ops.LoadConst:
                self.stack.append(self.consts[op.index])

            elif type(op) == ops.LoadName:
                lvar = self.vars[op.index]
                value = self.env.get(lvar)
                if value is None:
                    value = getattr(builtin, 'lua_' + lvar.value)
                self.stack.append(value)

            elif type(op) == ops.StoreName:
                var = self.vars[op.index]
                val = self.stack.pop()
                if type(val) == obj.LVar:
                    val = self.env[val]
                self.env[var] = val

            self.pc += 1

        return self
