"""Small, dependency-free contact-detail extractor."""

from __future__ import annotations

import re
from typing import Any

EMAIL_PATTERN = re.compile(
    r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+(?![\w.+-])"
)
PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+?\d{1,3}[ .-]?)?(?:\(?\d{2,4}\)?[ .-]?)?"
    r"\d{3,4}[ .-]\d{4}(?!\w)"
)
LINKEDIN_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?linkedin\.com/in/[\w-]+/?",
    re.IGNORECASE,
)
GITHUB_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/[\w-]+/?",
    re.IGNORECASE,
)


def extract_contact_details(text: str) -> dict[str, Any]:
    """Return contact data found in the resume text."""

    first_lines = [line.strip() for line in text.splitlines() if line.strip()][:5]

    name = ""
    for line in first_lines:
        if (
            not EMAIL_PATTERN.search(line)
            and not PHONE_PATTERN.search(line)
            and len(line) <= 80
        ):
            name = line
            break

    def unique(matches: list[str]) -> list[str]:
        return list(
            dict.fromkeys(match.rstrip("/.,; ") for match in matches)
        )

    return {
        "name": name,
        "emails": unique(EMAIL_PATTERN.findall(text)),
        "phones": unique(PHONE_PATTERN.findall(text)),
        "linkedin": unique(LINKEDIN_PATTERN.findall(text)),
        "github": unique(GITHUB_PATTERN.findall(text)),
    }