from pydantic.dataclasses import dataclass


@dataclass
class Page:
    chapter: int
    verse: int
