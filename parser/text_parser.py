"""Parser for .txt resume files."""

from __future__ import annotations

from pathlib import Path


class TextParser:
    supported_suffixes = {".txt"}

    def parse(self, path: str | Path) -> str:
        file_path = Path(path)

        for encoding in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
            try:
                return file_path.read_text(encoding=encoding).strip()
            except UnicodeDecodeError:
                continue

        raise ValueError("The text file could not be decoded.")