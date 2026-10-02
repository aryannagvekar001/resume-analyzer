from ..ai_analyzer import AIAnalyzer


class ProjectRewriter:
    def __init__(self):
        self.ai = AIAnalyzer()

    def rewrite(self, project_text):
        return self.ai.improve_resume(project_text)