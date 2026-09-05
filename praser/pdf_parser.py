"""Parser for text-based PDF resumes."""

from __future__ import annotations

from pathlib import Path


class PdfParser:
    supported_suffixes = {".pdf"}

    def parse(self, path: str | Path) -> str:
        try:
            from PyPDF2 import PdfReader
        except ImportError as error:
            raise RuntimeError(
                "PyPDF2 is required. Run: pip install PyPDF2"
            ) from error

        reader = PdfReader(str(path))

        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as error:
                raise ValueError(
                    "The PDF is encrypted and cannot be read."
                ) from error

        pages = [
            (page.extract_text() or "").strip()
            for page in reader.pages
        ]

        return "\n".join(page for page in pages if page).strip()