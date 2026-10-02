class ActionVerbAnalyzer:
    VERBS={"built","created","designed","developed","implemented","improved","managed","led","optimized"}
    def analyze(self,text): return {"verbs":sorted(v for v in self.VERBS if v in (text or "").lower().split())}
