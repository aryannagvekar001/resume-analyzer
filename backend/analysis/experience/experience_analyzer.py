from .action_verb_analyzer import ActionVerbAnalyzer
from .achievement_analyzer import AchievementAnalyzer
from .bullet_analyzer import BulletAnalyzer
from .impact_analyzer import ImpactAnalyzer


class ExperienceAnalyzer:

    def __init__(self):
        self.actions = ActionVerbAnalyzer()
        self.achievements = AchievementAnalyzer()
        self.bullets = BulletAnalyzer()
        self.impact = ImpactAnalyzer()

    def analyze(self, text):
        return {
            "actions": self.actions.analyze(text),
            "achievements": self.achievements.analyze(text),
            "bullets": self.bullets.analyze(text),
            "impact": self.impact.analyze(text),
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
