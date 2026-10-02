import re


class KeywordDensity:

    def calculate(self, text, keywords):
        words = re.findall(
            r"\b[\w+#.-]+\b",
            (text or "").lower(),
        )

        if not words:
            return 0

        count = sum(
            words.count(keyword.lower())
            for keyword in keywords or []
        )

        return round(
            count / len(words) * 100,
            2,
        )