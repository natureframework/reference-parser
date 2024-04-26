# Bible Citation Parser Library

The Bible Citation Parser Library is a specialized tool designed to interpret and extract structured information from citations of the Bible, specifically focusing on the four Gospels: Matthew, Mark, Luke, and John. This library is tailored to handle citations that refer to a single block of contiguous text, which may span across multiple chapters and verses. The citation format supported by this library is custom-made and does not conform to any existing standard citation formats.

## Supported Formats

The library supports three main formats for citations:

1. **Single Verse**: Identifies a specific verse within a chapter of a book.
   - Format: `book chapter:verse`
   - Example: `matthew 05:07`

2. **Spanning Multiple Verses**: Refers to a range of verses within the same chapter.
   - Format: `book chapter:verse_start-verse_end`
   - Example: `luke 15:01-10`

3. **Spanning Multiple Chapters**: Covers a range that extends across chapters.
   - Format: `book chapter_start:verse_start-chapter_end:verse_end`
   - Example: `mark 02:05-03:12`

### Requirements

- Python version: 3.9 or above.
- Installation: The library can be installed via pip directly from the GitHub repository.

### Installation

To install the library, use the following pip command:

```sh
pip install git+https://github.com/natureframework/citation-parser.git
```

## How to Use

Below are examples demonstrating how to use the Bible Citation Parser Library to parse different types of citations.

### Parsing a Simple Citation

```python
from citationparser import parse

citation = parse("john 03:16")
print(citation.book)  # Output: john
print(citation.start.chapter)  # Output: 3
print(citation.start.verse)  # Output: 16
print(citation.end.chapter)  # Output: 3
print(citation.end.verse)  # Output: 16
```

### Parsing a Citation Spanning Multiple Verses

```python
from citationparser import parse

citation = parse("mark 01:01-02")
print(citation.start.chapter)  # Output: 1
print(citation.start.verse)  # Output: 1
print(citation.end.chapter)  # Output: 1
print(citation.end.verse)  # Output: 2
```

### Parsing a Citation Spanning Multiple Chapters and Verses

```python
from citationparser import parse

citation = parse("john 28:19-29:20")
print(citation.start.chapter)  # Output: 28
print(citation.start.verse)  # Output: 19
print(citation.end.chapter)  # Output: 29
print(citation.end.verse)  # Output: 20
```

## Notes

- The book names must be in all lowercase for simplicity and consistency.
- Chapter and verse numbers must be composed of two digits (e.g., `01`) for proper sorting.
- This library is specifically designed for parsing citations from the Gospels only to keep the parsing rules simple.
- The format is designed to be limited and strict to reduce human errors in typing the citations and to simplify the underlying code to minimize the occurrence of bugs.
