from .project_technology import ProjectTechnology
from .project_impact import ProjectImpact
from .project_relevance import ProjectRelevance


class ProjectAnalyzer:

    def __init__(self):
        self.technology = ProjectTechnology()
        self.impact = ProjectImpact()
        self.relevance = ProjectRelevance()

    def analyze(self, text, job_description=""):
        return {
            "technologies": self.technology.extract(text),
            "impact": self.impact.analyze(text),
            "relevance": self.relevance.calculate(
                text,
                job_description,
            ),
        }