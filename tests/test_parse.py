from citationparser import parse


def test_simple():
    citation = parse("matthew 1:2")
    assert citation.book == "matthew"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end == citation.start


def test_span_verse():
    citation = parse("matthew 1:2-3")
    assert citation.book == "matthew"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 1
    assert citation.end.verse == 3


def test_span_chapter():
    citation = parse("matthew 1:2-3:4")
    assert citation.book == "matthew"
    assert citation.start.chapter == 1
    assert citation.start.verse == 2
    assert citation.end.chapter == 3
    assert citation.end.verse == 4
