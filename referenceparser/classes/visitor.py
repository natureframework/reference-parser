from parsimonious.nodes import NodeVisitor
from .page import Page
from .reference import Reference
from .span import Span


class Visitor(NodeVisitor):
    def visit_citation(self, _, visited_children):
        book, _, span = visited_children
        return Reference(book=book, start=span.start, end=span.end)

    def visit_span(self, _, visited_children):
        (value,) = visited_children
        if isinstance(value, Page):
            start = end = value
        else:
            start, _, end = value
            if isinstance(end, int):
                end = Page(chapter=start.chapter, verse=end)
        return Span(start=start, end=end)

    def visit_end(self, _, visited_children):
        (value,) = visited_children
        return value

    def visit_reference(self, _, visited_children):
        chapter, _, verse = visited_children
        return Page(chapter=chapter, verse=verse)

    def visit_number(self, node, _):
        return int(node.text)

    def visit_book(self, node, _):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node
