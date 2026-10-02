class TechnicalSkills:

    SKILLS = {
        "python", "java", "javascript", "typescript",
        "c", "c++", "sql", "mysql", "mongodb",
        "html", "css", "react", "node.js",
        "fastapi", "flask", "git", "docker",
        "aws", "azure", "tensorflow", "pandas",
        "tableau", "excel",
    }

    def extract(self, text):
        normalized = (text or "").lower()

        return sorted(
            skill
            for skill in self.SKILLS
            if f" {skill} " in f" {normalized} "
        )