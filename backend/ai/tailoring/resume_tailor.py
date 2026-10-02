from ..ai_analyzer import AIAnalyzer


class ResumeTailor:
    def __init__(self):
        self.ai = AIAnalyzer()

    def tailor(self, resume_text, job_description):
        return self.ai.tailor(
            resume_text,
            job_description,
        )