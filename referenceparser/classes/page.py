from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Page:
    chapter: int
    verse: int
