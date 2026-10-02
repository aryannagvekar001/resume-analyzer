import re


class ImpactAnalyzer:

    def analyze(self, text):
        lines = [
            line
            for line in (text or "").splitlines()
            if line.strip()
        ]

        impact_lines = [
            line
            for line in lines
            if re.search(
                r"\d+%|\d+\+?|increased|reduced|improved|saved",
                line,
                re.I,
            )
        ]

        return {
            "impact_lines": len(impact_lines),
            "has_impact": bool(impact_lines),
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
