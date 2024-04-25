from citationparser import parse


def test_simple():
    parse("matthew 1:2")


def test_range():
    parse("matthew 1:2-3")
