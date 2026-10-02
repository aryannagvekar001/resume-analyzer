class SkillRoadmap:

    def build(self, current_skills, target_role):
        current = {
            skill.lower()
            for skill in current_skills or []
        }

        required = {
            "python": {"python"},
            "sql": {"sql"},
            "git": {"git"},
            "cloud": {"aws", "azure"},
            "frontend": {
                "html",
                "css",
                "javascript",
                "react",
            },
            "ai": {
                "python",
                "tensorflow",
                "pandas",
            },
        }

        roadmap = []

        for name, skills in required.items():
            missing = skills - current

            if missing:
                roadmap.append({
                    "area": name,
                    "skills": sorted(missing),
                })

        return {
            "target_role": target_role,
            "roadmap": roadmap,
        }
