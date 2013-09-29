from luna import objects as obj
from luna.ast.visitors import GenericVisitor
from luna.vm import opcodes as ops
from luna.vm.frame import Frame


class Compiler(GenericVisitor):
    def __init__(self):
        self.code = []
        self.consts = []

    def compile(self, node):
        self.visit(node)
        return Frame(self.code, self.consts)

    def generic_visit(self, node, vc):
        return vc


    def add_const(self, luavalue):
        try:
            return self.consts.index(luavalue)
        except ValueError:
            self.consts.append(luavalue)
            return len(self.consts) - 1

    def emit(self, opcode):
        self.code.append(opcode)


    def visit_assignment(self, node, vc):
        ## TODO: right could be an expr, not a number
        left, [right] = vc
        i = self.add_const(left)
        j = self.add_const(right)
        self.emit(ops.LoadConst(i))
        self.emit(ops.LoadConst(j))
        self.emit(ops.StoreName())

    def visit_binop(self, node, vc):
        left, o, right = vc
        i = self.add_const(left)
        j = self.add_const(right)
        self.emit(ops.LoadConst(i))
        self.emit(ops.LoadConst(j))
        self.emit(ops.BinaryAdd())

    def visit_call(self, node, vc):
        func, [[args]] = vc
        i = self.add_const(func)
        self.emit(ops.LoadConst(i))
        # how to handle multiple args?
        for arg in args:
            j = self.add_const(arg)
            self.emit(ops.LoadConst(j))
        self.emit(ops.Call())

    def visit_identifier(self, node, vc):
        return obj.LVar(node.value)

    def visit_number(self, node, vc):
        return obj.LNumber(float(node.value))
