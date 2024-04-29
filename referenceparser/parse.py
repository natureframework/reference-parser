from .grammar import grammar
from .visitor import visitor


def parse(text: str) -> dict:
    tree = grammar.parse(text)
    return visitor.visit(tree)
