# Bible Reference Parser Library

The Bible Reference Parser Library is a specialized tool designed to interpret and extract structured information from references of the Bible. This library is tailored to handle references that refer to a single block of contiguous text, which may span across multiple chapters and verses. The reference format supported by this library is custom-made and does not conform to any existing standard reference formats.

## Supported Formats

The library supports three main formats for references:

1. **Single Verse**: Identifies a specific verse within a chapter of a book.
   - Format: `book chapter verse`
   - Example: `matthew 5 7`

2. **Spanning Multiple Verses**: Refers to a range of verses within the same chapter.
   - Format: `book chapter verse-verse`
   - Example: `luke 15 1-10`

3. **Spanning Multiple Chapters**: Covers a range that extends across chapters.
   - Format: `book chapter verse-chapter verse`
   - Example: `mark 2 5-3 12`

### Requirements

- Python version: 3.9 or above.
- Installation: The library can be installed via pip directly from the GitHub repository.

### Installation

To install the library, use the following pip command:

```sh
pip install git+https://github.com/natureframework/reference-parser.git
```

## How to Use

Below are examples demonstrating how to use the Bible Reference Parser Library to parse different types of references.

### Parsing a Simple Reference

```python
from referenceparser import parse

reference = parse("john 3 16")
print(reference.book)  # Output: john
print(reference.start.chapter)  # Output: 3
print(reference.start.verse)  # Output: 16
print(reference.end.chapter)  # Output: 3
print(reference.end.verse)  # Output: 16
```

### Parsing a Reference Spanning Multiple Verses

```python
from referenceparser import parse

reference = parse("mark 1 1-2")
print(reference.start.chapter)  # Output: 1
print(reference.start.verse)  # Output: 1
print(reference.end.chapter)  # Output: 1
print(reference.end.verse)  # Output: 2
```

### Parsing a Reference Spanning Multiple Chapters and Verses

```python
from referenceparser import parse

reference = parse("john 28 19-29 20")
print(reference.start.chapter)  # Output: 28
print(reference.start.verse)  # Output: 19
print(reference.end.chapter)  # Output: 29
print(reference.end.verse)  # Output: 20
```

### Parsing a Book Name with Multiple Words

```python
from referenceparser import parse

reference = parse("song of solomon 2 10-14")
print(reference.book)  # Output: song of solomon
print(reference.start.chapter)  # Output: 2
print(reference.start.verse)  # Output: 10
print(reference.end.chapter)  # Output: 2
print(reference.end.verse)  # Output: 14
```
