# Bible Citation Parser Library

A Python library designed to parse a citation that refers to a single block of contiguous text that can span multiple chapters.

The library supports parsing citations in the following formats:

1. `<book> <chapter>:<verse>`
2. `<book> <chapter>:<verse>-<verse>`
3. `<book> <chapter>:<verse>-<chapter>:<verse>`

## Installation

To install the Bible Citation Parser library, you will need to have Python installed on your system. The library requires Python 3.9 or newer. You can install the library directly from the GitHub repository using pip. Open your terminal or command prompt and run the following command:

```sh
pip install git+https://github.com/natureframework/citation-parser.git
```

This command tells pip to install the library directly from the specified GitHub URL.

## Basic Usage

Once installed, you can start using the library to parse Bible citations.

Here's a simple example of how to use the library:

```python
from citationparser import parse

# Parse a simple citation
citation = parse("John 3:16")
print(citation.book)  # Output: John
print(citation.start.chapter)  # Output: 3
print(citation.start.verse)  # Output: 16
print(citation.end.chapter)  # Output: 3
print(citation.end.verse)  # Output: 16

# Parse a citation spanning multiple verses
citation = parse("Genesis 1:1-2")
print(citation.start.chapter)  # Output: 1
print(citation.start.verse)  # Output: 1
print(citation.end.chapter)  # Output: 1
print(citation.end.verse)  # Output: 2

# Parse a citation spanning multiple chapters and verses
citation = parse("Matthew 28:19-29:20")
print(citation.start.chapter)  # Output: 28
print(citation.start.verse)  # Output: 19
print(citation.end.chapter)  # Output: 29
print(citation.end.verse)  # Output: 20
```
