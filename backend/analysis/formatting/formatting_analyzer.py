from .readability_analyzer import ReadabilityAnalyzer
from .structure_analyzer import StructureAnalyzer


class FormattingAnalyzer:

    def __init__(self):
        self.readability = ReadabilityAnalyzer()
        self.structure = StructureAnalyzer()

    def analyze(self, text):
        return {
            "readability": self.readability.analyze(text),
            "structure": self.structure.analyze(text),
        }