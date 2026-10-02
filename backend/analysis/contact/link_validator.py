import re


class LinkValidator:

    PATTERNS = {
        "linkedin": r"linkedin\.com/",
        "github": r"github\.com/",
    }

    def validate(self, links):
        result = {}

        for name, pattern in self.PATTERNS.items():
            result[name] = any(
                re.search(
                    pattern,
                    link,
                    re.I,
                )
                for link in links or []
            )

        return result