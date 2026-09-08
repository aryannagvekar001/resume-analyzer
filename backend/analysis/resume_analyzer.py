# analysis/resume_analyzer.py
import re

from .resume_score import ResumeScore
from .ats.ats_analyzer import ATSAnalyzer


class ResumeAnalyzer:
    KNOWN_SKILLS = {
        "aws", "azure", "c", "c++", "css", "docker", "excel",
        "fastapi", "flask", "git", "go", "html", "java",
        "javascript", "mongodb", "mysql", "node.js", "pandas",
        "python", "react", "sql", "tableau", "tensorflow",
        "typescript",
    }

    def __init__(self):
        self.resume_score = ResumeScore()
        self.ats_analyzer = ATSAnalyzer()

    def analyze(self, resume_text, job_description=""):
        text = (resume_text or "").strip()
        skills = self.extract_skills(text)

        quality = self.resume_score.calculate(text, skills)
        ats = self.ats_analyzer.analyze(text, job_description)

        return {
            "resume_score": quality["score"],
            "score_breakdown": quality["breakdown"],
            "skills": skills,
            "suggestions": quality["suggestions"],
            "word_count": quality["word_count"],
            "ats": ats,
        }

    def extract_skills(self, resume_text):
        normalized = (resume_text or "").lower()

        return sorted(
            skill
            for skill in self.KNOWN_SKILLS
            if re.search(
                r"(?<!\w)" + re.escape(skill) + r"(?!\w)",
                normalized,
            )
        )