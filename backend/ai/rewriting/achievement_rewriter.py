from ..ai_analyzer import AIAnalyzer


class AchievementRewriter:
    def __init__(self):
        self.ai = AIAnalyzer()

    def rewrite(self, achievement):
        return self.ai.improve_resume(achievement)