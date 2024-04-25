from parsimonious.nodes import NodeVisitor
from .reference import Reference
from .citation import Citation
from .span import Span


class Visitor(NodeVisitor):
    def visit_citation(self, _, visited_children):
        book, _, span = visited_children
        return Citation(book=book, start=span.start, end=span.end)

    def visit_span(self, _, visited_children):
        (value,) = visited_children
        if isinstance(value, Reference):
            start = end = value
        else:
            start, _, end = value
            if isinstance(end, int):
                end = Reference(chapter=start.chapter, verse=end)
        return Span(start=start, end=end)

    def visit_end(self, _, visited_children):
        (value,) = visited_children
        return value

    def visit_reference(self, _, visited_children):
        chapter, _, verse = visited_children
        return Reference(chapter=chapter, verse=verse)

    def visit_number(self, node, _):
        return int(node.text)

    def visit_word(self, node, _):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node
