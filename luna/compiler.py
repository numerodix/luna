from luna import objects as obj
from luna.ast.visitors import GenericVisitor
from luna.vm import opcodes as ops
from luna.vm.frame import Frame


class Compiler(GenericVisitor):
    def __init__(self):
        self.code = []
        self.consts = []
        self.vars = []

        self.binops = {
            '+': ops.BinaryAdd,
            '-': ops.BinarySubtract,
        }

    def compile(self, node):
        self.visit(node)
        return Frame(self.code, self.consts, self.vars)

    def generic_visit(self, node, vc):
        return vc


    def add_const(self, luavalue):
        try:
            return self.consts.index(luavalue)
        except ValueError:
            self.consts.append(luavalue)
            return len(self.consts) - 1

    def add_var(self, luavalue):
        try:
            return self.vars.index(luavalue)
        except ValueError:
            self.vars.append(luavalue)
            return len(self.vars) - 1

    def emit(self, opcode):
        self.code.append(opcode)


    def add_operand(self, val):
        if type(val) == obj.LVar:
            i = self.add_var(val)
            self.emit(ops.LoadName(i))
        else:
            i = self.add_const(val)
            self.emit(ops.LoadConst(i))
        return i


    def visit_assignment(self, node, vc):
        left, [right] = vc
        if right:
            j = self.add_operand(right)
        i = self.add_var(left)
        self.emit(ops.StoreName(i))

    def visit_arith(self, node, vc):
        left, _, right = vc
        op = node.op
        if left:
            i = self.add_operand(left)
        if right:
            j = self.add_operand(right)
        opclass = self.binops[op.pyvalue]
        self.emit(opclass())

    def visit_call(self, node, vc):
        func, [args] = vc
        # how to handle multiple args?
        for arg in args:
            if arg:
                j = self.add_operand(arg)
        i = self.add_operand(func)
        self.emit(ops.Call())

    def visit_identifier(self, node, vc):
        return obj.LVar(node.value)

    def visit_number(self, node, vc):
        return obj.LNumber(float(node.value))
