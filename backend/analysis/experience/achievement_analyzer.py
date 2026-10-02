import re


class AchievementAnalyzer:

    def analyze(self, text):
        lines = [
            line.strip()
            for line in (text or "").splitlines()
            if line.strip()
        ]

        measurable = [
            line
            for line in lines
            if re.search(
                r"\d+%|\d+\+?|\$[\d,]+",
                line,
            )
        ]

        return {
            "total_lines": len(lines),
            "measurable_lines": len(measurable),
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
