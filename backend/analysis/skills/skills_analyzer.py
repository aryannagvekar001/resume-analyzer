from .technical_skills import TechnicalSkills
from .soft_skills import SoftSkills
from .skill_categorizer import SkillCategorizer
from .skill_strength import SkillStrength


class SkillsAnalyzer:

    def __init__(self):
        self.technical = TechnicalSkills()
        self.soft = SoftSkills()
        self.categorizer = SkillCategorizer()
        self.strength = SkillStrength()

    def analyze(self, text):
        technical = self.technical.extract(text)
        soft = self.soft.extract(text)

        categories = self.categorizer.categorize(
            technical,
            soft,
        )

        all_skills = technical + soft

        return {
            "technical": technical,
            "soft": soft,
            "categories": categories,
            "strength": self.strength.calculate(
                all_skills
            ),
        }