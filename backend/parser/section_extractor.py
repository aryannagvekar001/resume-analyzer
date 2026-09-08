"""Resume section detection from extracted plain text."""

from __future__ import annotations

import re

SECTION_ALIASES = {
    "summary": {
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective",
    },
    "experience": {
        "experience",
        "work experience",
        "professional experience",
        "employment history",
    },
    "education": {
        "education",
        "academic background",
        "qualifications",
    },
    "skills": {
        "skills",
        "technical skills",
        "core competencies",
        "competencies",
    },
    "projects": {
        "projects",
        "personal projects",
        "academic projects",
    },
    "certifications": {
        "certifications",
        "certificates",
        "licenses",
    },
    "achievements": {
        "achievements",
        "awards",
        "accomplishments",
    },
}

HEADING_MAP = {
    alias.casefold(): canonical
    for canonical, aliases in SECTION_ALIASES.items()
    for alias in aliases
}


def _normalise_heading(line: str) -> str:
    return re.sub(r"[^a-z ]", "", line.casefold()).strip()


def extract_sections(text: str) -> dict[str, str]:
    """Split a resume into common sections."""

    sections: dict[str, list[str]] = {"other": []}
    current_section = "other"

    for raw_line in text.splitlines():
        line = raw_line.strip()

        heading = None
        if line and len(line) <= 60:
            heading = HEADING_MAP.get(_normalise_heading(line))

        if heading:
            current_section = heading
            sections.setdefault(current_section, [])
        else:
            sections[current_section].append(raw_line.rstrip())

    return {
        section_name: "\n".join(lines).strip()
        for section_name, lines in sections.items()
        if "\n".join(lines).strip()
    }