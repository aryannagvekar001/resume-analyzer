from ..ai_analyzer import AIAnalyzer


class ResumeRewriter:
    def __init__(self):
        self.ai = AIAnalyzer()

    def rewrite(self, resume_text):
        return self.ai.improve_resume(resume_text)