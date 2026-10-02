from .project_technology import ProjectTechnology
class ProjectAnalyzer:
    def __init__(self): self.technology=ProjectTechnology()
    def analyze(self,text,job=""): return {"technologies":self.technology.extract(text)}
