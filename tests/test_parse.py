from pytest import raises
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


def test_two_digits():
    citation = parse("matthew 10 11")
    assert citation.book == "matthew"
    assert citation.start.chapter == 10
    assert citation.start.verse == 11
    assert citation.end == citation.start


def test_multiple_words():
    citation = parse("1 corinthians 1 2-3 4")
    assert citation.book == "1 corinthians"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 3
    assert citation.end.verse == 4


def test_invalid_pattern():
    with raises(ValueError):
        parse("a b c")


def test_hash():
    assert hash(parse("matthew 1 1"))
