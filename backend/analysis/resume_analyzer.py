import re

from .resume_score import ResumeScore
from .ats.ats_analyzer import ATSAnalyzer
from .skills.skills_analyzer import SkillsAnalyzer
from .keywords.keyword_analyzer import KeywordAnalyzer
from .experience.experience_analyzer import ExperienceAnalyzer
from .projects.project_analyzer import ProjectAnalyzer
from .education.education_analyzer import EducationAnalyzer
from .education.certification_analyzer import CertificationAnalyzer
from .formatting.formatting_analyzer import FormattingAnalyzer
from .contact.contact_analyzer import ContactAnalyzer


class ResumeAnalyzer:

    KNOWN_SKILLS = {
        "aws", "azure", "c", "c++", "css", "docker",
        "excel", "fastapi", "flask", "git", "go",
        "html", "java", "javascript", "mongodb",
        "mysql", "node.js", "pandas", "python",
        "react", "sql", "tableau", "tensorflow",
        "typescript",
    }

    def __init__(self):
        self.resume_score = ResumeScore()
        self.ats = ATSAnalyzer()
        self.skills = SkillsAnalyzer()
        self.keywords = KeywordAnalyzer()
        self.experience = ExperienceAnalyzer()
        self.projects = ProjectAnalyzer()
        self.education = EducationAnalyzer()
        self.certifications = CertificationAnalyzer()
        self.formatting = FormattingAnalyzer()
        self.contact = ContactAnalyzer()

    def analyze(self, resume_text, job_description=""):
        text = (resume_text or "").strip()

        skills = self.extract_skills(text)

        quality = self.resume_score.calculate(
            text,
            skills,
        )

        return {
            "resume_score": quality["score"],
            "score_breakdown": quality["breakdown"],
            "suggestions": quality["suggestions"],
            "word_count": quality["word_count"],
            "skills": skills,
            "skills_analysis": self.skills.analyze(text),
            "keywords": self.keywords.analyze(
                text,
                job_description,
            ),
            "experience": self.experience.analyze(text),
            "projects": self.projects.analyze(
                text,
                job_description,
            ),
            "education": self.education.analyze(text),
            "certifications": self.certifications.analyze(text),
            "formatting": self.formatting.analyze(text),
            "contact_analysis": self.contact.analyze(text),
            "ats": self.ats.analyze(
                text,
                job_description,
            ),
        }

    def extract_skills(self, resume_text):
        normalized = (resume_text or "").lower()

        return sorted(
            skill
            for skill in self.KNOWN_SKILLS
            if re.search(
                r"(?<!\w)"
                + re.escape(skill)
                + r"(?!\w)",
                normalized,
            )
        )