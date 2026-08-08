import re


COMMON_SKILLS = [
    "python",
    "java",
    "javascript",
    "c++",
    "sql",
    "html",
    "css",
    "react",
    "node.js",
    "fastapi",
    "django",
    "flask",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "gcp",
    "mongodb",
    "mysql",
    "postgresql",
]


def detect_skills(text):

    text_lower = text.lower()

    detected = []

    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            detected.append(skill)

    return detected


def calculate_resume_score(text):

    score = 0

    sections = {
        "education": ["education", "academic"],
        "experience": ["experience", "employment", "work history"],
        "skills": ["skills", "technical skills"],
        "projects": ["projects", "project"],
        "certifications": ["certification", "certifications"],
    }

    text_lower = text.lower()

    for keywords in sections.values():

        if any(keyword in text_lower for keyword in keywords):
            score += 15

    if len(text.split()) > 300:
        score += 10

    return min(score, 100)