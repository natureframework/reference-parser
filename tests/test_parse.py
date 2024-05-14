from pytest import raises
from parsimonious.exceptions import ParseError
from referenceparser import parse


def test_simple():
    citation = parse("matthew 1 2")
    assert citation.book == "matthew"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end == citation.start


def test_span_verse():
    citation = parse("mark 1 2-3")
    assert citation.book == "mark"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 1
    assert citation.end.verse == 3


def test_span_chapter():
    citation = parse("luke 1 2-3 4")
    assert citation.book == "luke"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 3
    assert citation.end.verse == 4


def test_books():
    assert parse("matthew 1 1").book == "matthew"
    assert parse("mark 1 1").book == "mark"
    assert parse("luke 1 1").book == "luke"
    assert parse("john 1 1").book == "john"


def test_unknown_book():
    with raises(ParseError):
        parse("unknown 1 1")


def test_zero_number():
    with raises(ParseError):
        parse("matthew 0 0")


def test_two_digits():
    citation = parse("matthew 10 11")
    assert citation.book == "matthew"
    assert citation.start.chapter == 10
    assert citation.start.verse == 11
    assert citation.end == citation.start
