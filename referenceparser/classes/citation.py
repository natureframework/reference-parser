from pydantic.dataclasses import dataclass
from .span import Span


@dataclass
class Citation(Span):
    book: str
