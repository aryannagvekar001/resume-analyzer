from ..ai_analyzer import AIAnalyzer


class SummaryGenerator:
    def __init__(self):
        self.ai = AIAnalyzer()

    def generate(self, resume_text):
        return self.ai.summarize(resume_text)