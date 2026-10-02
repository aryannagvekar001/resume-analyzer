class LearningRecommender:

    TOPICS = {
        "python": "Python programming and automation",
        "sql": "SQL and database fundamentals",
        "git": "Git and GitHub",
        "aws": "AWS cloud fundamentals",
        "azure": "Microsoft Azure fundamentals",
        "react": "React frontend development",
        "tensorflow": "Machine learning with TensorFlow",
        "pandas": "Data analysis with Pandas",
        "fastapi": "FastAPI backend development",
    }

    def recommend(self, missing_skills):
        return [
            {
                "skill": skill,
                "topic": self.TOPICS.get(
                    skill.lower(),
                    f"Learn {skill}",
                ),
            }
            for skill in missing_skills or []
        ]