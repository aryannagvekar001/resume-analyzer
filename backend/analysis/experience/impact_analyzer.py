import re
class ImpactAnalyzer:
    def analyze(self,text): return {"has_impact":bool(re.search(r"\\d+%|increased|reduced|improved",text or "",re.I))}
