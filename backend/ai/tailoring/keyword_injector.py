import re


class KeywordInjector:

    def inject(self, text, keywords):
        text = text or ""

        missing = []

        for keyword in keywords or []:
            pattern = re.escape(keyword)

            if not re.search(
                rf"(?<!\w){pattern}(?!\w)",
                text,
                re.IGNORECASE,
            ):
                missing.append(keyword)

        if not missing:
            return text

        addition = "\n\nRelevant Skills: " + ", ".join(missing)

        return text.rstrip() + addition