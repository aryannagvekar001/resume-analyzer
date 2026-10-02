import re

from .keyword_density import KeywordDensity
from .keyword_strength import KeywordStrength
from .keyword_relevance import KeywordRelevance


class KeywordAnalyzer:

    def __init__(self):
        self.density = KeywordDensity()
        self.strength = KeywordStrength()
        self.relevance = KeywordRelevance()

    def analyze(self, text, job_description=""):
        resume_words = self._words(text)
        job_words = self._words(job_description)

        matched = sorted(
            set(resume_words) & set(job_words)
        )

        return {
            "matched": matched,
            "density": self.density.calculate(
                text,
                matched,
            ),
            "strength": self.strength.calculate(
                matched
            ),
            "relevance": self.relevance.calculate(
                matched,
                job_words,
            ),
        }

    @staticmethod
    def _words(text):
        return re.findall(
            r"[a-zA-Z][a-zA-Z0-9+#.-]*",
            (text or "").lower(),
        )