import re
class AchievementAnalyzer:
    def analyze(self,text): return {"measurable_lines":sum(bool(re.search(r"\\d+%|\\d+\\+?",x)) for x in (text or "").splitlines())}
