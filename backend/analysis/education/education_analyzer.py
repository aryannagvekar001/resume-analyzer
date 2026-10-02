import re
class EducationAnalyzer:
    def analyze(self,text): return {"has_education":bool(re.search(r"\\beducation\\b",text or "",re.I))}
