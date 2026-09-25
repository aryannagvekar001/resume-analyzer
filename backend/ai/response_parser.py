import re


class ResponseParser:

    @staticmethod
    def clean(text):
        text = (text or "").strip()

        text = re.sub(
            r"^```(?:text|markdown)?",
            "",
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(r"```$", "", text)

        return text.strip()

    @staticmethod
    def bullets(text):
        lines = []

        for line in (text or "").splitlines():
            line = line.strip()

            if not line:
                continue

            line = re.sub(r"^[-*•]\s*", "", line)
            lines.append(line)

        return lines
