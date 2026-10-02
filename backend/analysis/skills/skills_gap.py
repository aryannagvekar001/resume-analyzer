class SkillsGap:

    def compare(self, resume_skills, required_skills):
        resume = {
            skill.lower()
            for skill in resume_skills or []
        }

        required = {
            skill.lower()
            for skill in required_skills or []
        }

        return {
            "matched": sorted(resume & required),
            "missing": sorted(required - resume),
        }