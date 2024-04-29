from pydantic.dataclasses import dataclass
from .span import Span


@dataclass
class Reference(Span):
    book: str
