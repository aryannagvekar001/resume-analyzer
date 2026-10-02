class SkillMatcher:
    def match(self,resume_skills,required_skills):
        a={x.lower() for x in resume_skills or []}; b={x.lower() for x in required_skills or []}; return {"matched":sorted(a&b),"missing":sorted(b-a)}
