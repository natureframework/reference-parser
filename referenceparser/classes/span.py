from pydantic.dataclasses import dataclass
from .page import Page


@dataclass
class Span:
    start: Page
    end: Page
