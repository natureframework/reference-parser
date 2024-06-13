from .classes.reference import Reference
from .regex.matcher import matcher
from .classes.page import Page


def parse(pattern: str) -> Reference:
    match = matcher.match(pattern)
    if match:
        groups = match.groupdict()
        return Reference(
            book=groups["book"],
            start=Page(
                chapter=int(groups["chapter_start"]),
                verse=int(groups["chapter_start_verse_start"]),
            ),
            end=Page(
                chapter=int(groups["chapter_end"] or groups["chapter_start"]),
                verse=int(
                    groups["chapter_end_verse_end"]
                    or groups["chapter_start_verse_end"]
                    or groups["chapter_start_verse_start"]
                ),
            ),
        )
    raise ValueError(f"Invalid pattern: {pattern}")
