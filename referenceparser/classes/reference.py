from pydantic.dataclasses import dataclass
from .span import Span


@dataclass(frozen=True)
class Reference(Span):
    book: str
