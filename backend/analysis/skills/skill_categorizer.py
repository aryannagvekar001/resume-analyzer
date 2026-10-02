class SkillCategorizer:

    def categorize(self, technical, soft):
        return {
            "technical": sorted(set(technical or [])),
            "soft": sorted(set(soft or [])),
        }