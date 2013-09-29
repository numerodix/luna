from luna import objects as obj
from luna.ast.visitors import GenericVisitor
from luna.vm import opcodes as op
from luna.vm.frame import Frame


class Compiler(GenericVisitor):
    def __init__(self):
        self.code = []
        self.consts = []

    def compile(self, node):
        self.visit(node)
        return Frame(self.code, self.consts)

    def generic_visit(self, node, vc):
        pass


    def visit_binop(self, node, vc):
        self.code += [op.BinaryAdd()]

    def visit_number(self, node, vc):
        i = len(self.consts)
        self.code += [op.LoadConst(i)]
        self.consts += [obj.LNumber(float(node.value))]
