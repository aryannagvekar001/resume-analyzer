from backend.analysis.skills.skills_analyzer import SkillsAnalyzer

from .role_recommender import RoleRecommender
from .skill_roadmap import SkillRoadmap
from .learning_recommender import LearningRecommender
from .career_roadmap import CareerRoadmap


class CareerRecommender:

    def __init__(self):
        self.skills = SkillsAnalyzer()
        self.roles = RoleRecommender()
        self.skill_roadmap = SkillRoadmap()
        self.learning = LearningRecommender()
        self.roadmap = CareerRoadmap()

    def recommend(self, resume_text):
        skill_data = self.skills.analyze(
            resume_text
        )

        current_skills = (
            skill_data["technical"]
            + skill_data["soft"]
        )

        roles = self.roles.recommend(
            current_skills
        )

        primary_role = (
            roles[0]["role"]
            if roles
            else "Software Developer"
        )

        roadmap = self.skill_roadmap.build(
            current_skills,
            primary_role,
        )

        missing = []

        for item in roadmap["roadmap"]:
            missing.extend(
                item["skills"]
            )

        return {
            "current_skills": sorted(
                set(current_skills)
            ),
            "recommended_roles": roles,
            "skill_roadmap": roadmap,
            "learning_recommendations": (
                self.learning.recommend(missing)
            ),
            "career_roadmap": (
                self.roadmap.build(primary_role)
            ),
        }
