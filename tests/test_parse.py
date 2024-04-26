from pytest import raises
from parsimonious.exceptions import ParseError
from citationparser import parse


def test_simple():
    citation = parse("matthew 01:02")
    assert citation.book == "matthew"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end == citation.start


def test_span_verse():
    citation = parse("mark 01:02-03")
    assert citation.book == "mark"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 1
    assert citation.end.verse == 3


def test_span_chapter():
    citation = parse("luke 01:02-03:04")
    assert citation.book == "luke"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 3
    assert citation.end.verse == 4


def test_books():
    assert parse("matthew 01:01").book == "matthew"
    assert parse("mark 01:01").book == "mark"
    assert parse("luke 01:01").book == "luke"
    assert parse("john 01:01").book == "john"


def test_unknown_book():
    with raises(ParseError):
        parse("unknown 01:01")


def test_zero_number():
    with raises(ParseError):
        parse("matthew 00:00")
