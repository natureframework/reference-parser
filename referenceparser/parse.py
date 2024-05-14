from .classes.reference import Reference
from .grammar import grammar
from .visitor import visitor


def parse(text: str) -> Reference:
    tree = grammar.parse(text)
    return visitor.visit(tree)
