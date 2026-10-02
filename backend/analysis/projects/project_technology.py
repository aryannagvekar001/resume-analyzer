import re


class ProjectTechnology:

    def extract(self, text):
        technologies = {
            "python", "java", "javascript", "react",
            "fastapi", "flask", "docker", "aws",
            "azure", "sql", "mongodb", "tensorflow",
            "pandas", "git", "html", "css",
        }

        normalized = (text or "").lower()

        return sorted(
            tech
            for tech in technologies
            if re.search(
                rf"(?<!\w){re.escape(tech)}(?!\w)",
                normalized,
            )
        )