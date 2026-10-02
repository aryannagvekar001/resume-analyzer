import re

from .link_validator import LinkValidator


class ContactAnalyzer:

    def __init__(self):
        self.links = LinkValidator()

    def analyze(self, text):
        text = text or ""

        email = re.search(
            r"[\w.+-]+@[\w-]+\.[\w.-]+",
            text,
        )

        phone = re.search(
            r"\+?\d[\d\s().-]{7,}\d",
            text,
        )

        links = re.findall(
            r"https?://\S+",
            text,
        )

        return {
            "email": bool(email),
            "phone": bool(phone),
            "links": self.links.validate(links),
        }