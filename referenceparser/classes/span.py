from pydantic.dataclasses import dataclass
from .reference import Reference


@dataclass
class Span:
    start: Reference
    end: Reference
