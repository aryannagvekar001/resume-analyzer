class SoftSkills:

    SKILLS = {
        "communication",
        "leadership",
        "teamwork",
        "problem solving",
        "time management",
        "adaptability",
        "collaboration",
        "critical thinking",
        "communication skills",
    }

    def extract(self, text):
        normalized = (text or "").lower()

        return sorted(
            skill
            for skill in self.SKILLS
            if skill in normalized
        )