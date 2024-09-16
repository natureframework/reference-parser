from pydantic.dataclasses import dataclass
from .page import Page


@dataclass(frozen=True)
class Span:
    start: Page
    end: Page
