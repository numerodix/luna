from __future__ import print_function

from luna.interpreter import EnvBuilder
from luna.interpreter import EvalVisitor


def interpret(tree):
    envbuilder = EnvBuilder()
    envbuilder.visit(tree)

    env = envbuilder.env
    # seed a fake stdlib
    env.update({
        'print': print,
    })

    visitor = EvalVisitor(env)
    return visitor.visit(tree)
