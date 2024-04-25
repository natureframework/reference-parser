from pydantic.dataclasses import dataclass
from .span import Span


@dataclass
class Citation:
    book: str
    span: Span
