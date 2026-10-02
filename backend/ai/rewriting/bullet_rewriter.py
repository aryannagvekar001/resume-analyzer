from ..ai_analyzer import AIAnalyzer


class BulletRewriter:
    def __init__(self):
        self.ai = AIAnalyzer()

    def rewrite(self, bullet):
        result = self.ai.improve_resume(bullet)

        return result or bullet