from pydantic.dataclasses import dataclass


@dataclass
class Reference:
    chapter: int
    verse: int
