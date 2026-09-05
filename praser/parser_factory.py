"""Select a parser and create structured resume data."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .contact_extractor import extract_contact_details
from .docx_parser import DocxParser
from .pdf_parser import PdfParser
from .section_extractor import extract_sections
from .text_parser import TextParser


class ParserError(ValueError):
    """Raised when a resume cannot be parsed."""


_PARSERS = (
    PdfParser(),
    DocxParser(),
    TextParser(),
)


def get_parser(path: str | Path):
    """Return the correct parser for a file."""

    file_path = Path(path)
    suffix = file_path.suffix.casefold()

    for parser in _PARSERS:
        if suffix in parser.supported_suffixes:
            return parser

    supported = ", ".join(
        sorted(
            suffix
            for parser in _PARSERS
            for suffix in parser.supported_suffixes
        )
    )

    raise ParserError(
        f"Unsupported file type '{file_path.suffix or '(none)'}'. "
        f"Supported types: {supported}."
    )


def parse_resume(path: str | Path) -> dict[str, Any]:
    """
    Parse a PDF, DOCX, or TXT resume.

    Returns text, contact details, sections, and source metadata.
    """

    file_path = Path(path).expanduser()

    if not file_path.is_file():
        raise ParserError(f"Resume file was not found: {file_path}")

    try:
        text = get_parser(file_path).parse(file_path)
    except ParserError:
        raise
    except Exception as error:
        raise ParserError(
            f"Could not parse '{file_path.name}': {error}"
        ) from error

    if not text:
        raise ParserError(
            "No selectable text was found. "
            "The PDF may be a scanned image."
        )

    return {
        "source": {
            "path": str(file_path),
            "filename": file_path.name,
            "extension": file_path.suffix.casefold(),
        },
        "text": text,
        "contact": extract_contact_details(text),
        "sections": extract_sections(text),
    }