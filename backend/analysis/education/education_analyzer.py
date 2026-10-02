import re


class EducationAnalyzer:

    def analyze(self, text):
        normalized = (text or "").lower()

        degrees = []

        for degree in (
            "b.sc",
            "bsc",
            "b.tech",
            "btech",
            "m.sc",
            "msc",
            "m.tech",
            "mtech",
            "bachelor",
            "master",
            "phd",
        ):
            if re.search(
                rf"(?<!\w){re.escape(degree)}(?!\w)",
                normalized,
            ):
                degrees.append(degree)

        return {
            "degrees": sorted(set(degrees)),
            "has_education": bool(
                re.search(
                    r"\beducation\b",
                    normalized,
                )
            ),
        }