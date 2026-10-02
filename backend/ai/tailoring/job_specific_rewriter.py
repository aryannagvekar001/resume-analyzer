from ..ai_analyzer import AIAnalyzer


class JobSpecificRewriter:
    def __init__(self):
        self.ai = AIAnalyzer()

    def rewrite(self, resume_text, job_description):
        return self.ai.tailor(
            resume_text,
            job_description,
        )