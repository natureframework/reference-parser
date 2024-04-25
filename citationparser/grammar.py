from parsimonious.grammar import Grammar
from .constants.paths import GRAMMAR_FILE

grammar = Grammar(GRAMMAR_FILE.read_text(encoding="utf-8"))
