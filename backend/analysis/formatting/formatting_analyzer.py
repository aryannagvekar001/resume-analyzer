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
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
