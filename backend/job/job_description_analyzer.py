import re
class JobDescriptionAnalyzer:
    def analyze(self,text): return {"keywords":sorted(set(re.findall(r"[a-zA-Z][a-zA-Z0-9+#.-]*",(text or "").lower())))}
