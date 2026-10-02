import re


class ProjectImpact:

    def analyze(self, text):
        matches = re.findall(
            r"\d+%|\d+\+?|\d+x",
            text or "",
            re.I,
        )

        return {
            "measurable_results": len(matches),
            "values": matches,
        }