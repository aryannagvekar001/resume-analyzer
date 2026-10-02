from ..ai_analyzer import AIAnalyzer


class ImprovementGenerator:
    def __init__(self):
        self.ai = AIAnalyzer()

    def generate(self, resume_text):
        return self.ai.recommendations(resume_text)