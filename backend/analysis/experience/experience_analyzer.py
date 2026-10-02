from .action_verb_analyzer import ActionVerbAnalyzer
class ExperienceAnalyzer:
    def __init__(self): self.actions=ActionVerbAnalyzer()
    def analyze(self,text): return {"actions":self.actions.analyze(text)}
