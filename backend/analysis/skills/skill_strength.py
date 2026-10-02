class SkillStrength:

    def calculate(self, skills):
        count = len(skills or [])

        if count >= 12:
            level = "strong"
        elif count >= 6:
            level = "moderate"
        else:
            level = "developing"

        return {
            "count": count,
            "level": level,
        }