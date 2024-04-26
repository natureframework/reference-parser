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

## Design Constraints

The Design Constraints section outlines specific limitations and rules that govern how the Bible Citation Parser Library operates. These constraints are crucial for ensuring the library functions correctly and efficiently.

1. **Book Names in Lowercase**: Requiring all book names to be in lowercase serves several purposes. Firstly, it eliminates ambiguity and the potential for errors related to case sensitivity. By standardizing the input format, the library simplifies the parsing process. This constraint ensures consistency across all inputs, making it easier for users to remember how to format their citations and for the library to process them.

2. **Two-Digit Chapter and Verse Numbers**: Mandating that chapter and verse numbers be formatted with two digits (e.g., `01` instead of `1`) aims to facilitate proper sorting and uniformity. This formatting choice helps in distinguishing between single and multiple-digit numbers, ensuring that citations are parsed and sorted correctly, especially when dealing with ranges. It also contributes to the overall consistency of the citation format.

3. **Focus on the Gospels Only**: Limiting the scope of the library to parsing citations from the Gospels (Matthew, Mark, Luke, and John) significantly simplifies the parsing rules. The Gospels have a relatively uniform structure compared to other parts of the Bible, which can vary widely in their formatting and numbering. By focusing on a specific subset of the Bible, the library can offer more accurate and efficient parsing capabilities without the need to account for the complexities and exceptions present in other books.

4. **Strict and Limited Format**: Adopting a strict and limited format for citations reduces the likelihood of human error and simplifies the underlying code. By defining clear rules for how citations must be formatted, the library can more easily detect and parse the intended references. This constraint also helps in minimizing the occurrence of bugs by reducing the number of edge cases and variations the library needs to handle. A well-defined format ensures that users know exactly how to input their citations, leading to fewer errors and a smoother user experience.
