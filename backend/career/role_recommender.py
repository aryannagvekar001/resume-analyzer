class RoleRecommender:

    ROLE_SKILLS = {
        "Python Developer": {
            "python",
            "git",
            "sql",
            "fastapi",
        },
        "Data Analyst": {
            "python",
            "sql",
            "excel",
            "tableau",
        },
        "Frontend Developer": {
            "html",
            "css",
            "javascript",
            "react",
        },
        "Backend Developer": {
            "python",
            "fastapi",
            "sql",
            "git",
        },
        "AI/ML Engineer": {
            "python",
            "tensorflow",
            "pandas",
            "sql",
        },
    }

    def recommend(self, skills):
        skills = {
            skill.lower()
            for skill in skills or []
        }

        results = []

        for role, required in self.ROLE_SKILLS.items():
            matched = skills & required

            score = round(
                len(matched)
                / len(required)
                * 100
            )

            results.append({
                "role": role,
                "score": score,
                "matched_skills": sorted(matched),
                "missing_skills": sorted(
                    required - skills
                ),
            })

        return sorted(
            results,
            key=lambda item: item["score"],
            reverse=True,
        )
