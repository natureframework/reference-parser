from citationparser import parse


def test_simple():
    citation = parse("matthew 1:2")
    assert citation.book == "matthew"
    assert citation.span.start.chapter == 1
    assert citation.span.start.verse == 2
    assert citation.span.end == citation.span.start


def test_span_verse():
    citation = parse("matthew 1:2-3")
    assert citation.book == "matthew"
    assert citation.span.start.chapter == 1
    assert citation.span.start.verse == 2
    assert citation.span.end.chapter == 1
    assert citation.span.end.verse == 3


def test_span_chapter():
    citation = parse("matthew 1:2-3:4")
    assert citation.book == "matthew"
    assert citation.span.start.chapter == 1
    assert citation.span.start.verse == 2
    assert citation.span.end.chapter == 3
    assert citation.span.end.verse == 4
